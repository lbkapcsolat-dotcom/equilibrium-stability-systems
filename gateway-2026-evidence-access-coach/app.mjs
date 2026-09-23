const STOP = new Set(['a','an','the','is','are','was','were','be','been','being','to','of','for','and','or','in','on','at','by','with','from','that','this','it','as','into','than','then']);
const DOWN = new Set(['reduce','reduced','reduces','decrease','decreased','decreases','lower','lowered','less','decline','declined','drop','dropped']);
const UP = new Set(['increase','increased','increases','higher','more','rise','rose','rises','grow','grew','grown']);
const NEG = ['not','no','never','did not','does not','cannot','can\'t','without'];

function tokens(text){
  return String(text || '').toLowerCase().replace(/[^a-z0-9%]+/g,' ').trim().split(/\s+/).filter(Boolean);
}
function contentTokens(text){
  return tokens(text).filter(t => !STOP.has(t) && !DOWN.has(t) && !UP.has(t) && !NEG.includes(t));
}
function hasPhrase(text, phrases){
  const s = ` ${String(text||'').toLowerCase().replace(/[^a-z0-9%']+/g,' ')} `;
  return phrases.some(p => s.includes(` ${p} `));
}
function direction(text){
  const ts = new Set(tokens(text));
  if ([...DOWN].some(x => ts.has(x))) return 'DOWN';
  if ([...UP].some(x => ts.has(x))) return 'UP';
  return 'NONE';
}
function explicitNegation(text){ return hasPhrase(text, NEG); }

export function assessEvidence(claim, evidence){
  const c = String(claim || '').trim();
  const e = String(evidence || '').trim();
  if (!c || !e) return {
    relation:'INSUFFICIENT',
    reason:'Both a claim and an evidence excerpt are required.',
    next:'Add the missing claim or evidence excerpt before comparing them.'
  };

  const claimTerms = [...new Set(contentTokens(c))];
  const evidenceSet = new Set(contentTokens(e));
  const shared = claimTerms.filter(t => evidenceSet.has(t));
  const overlap = claimTerms.length ? shared.length / claimTerms.length : 0;

  if (shared.length < 2 || overlap < 0.34) return {
    relation:'INSUFFICIENT',
    reason:'The excerpt does not share enough specific content with the claim for this bounded comparison.',
    next:'Find a source excerpt that directly addresses the claim subject and outcome.'
  };

  const cDir = direction(c), eDir = direction(e);
  const cNeg = explicitNegation(c), eNeg = explicitNegation(e);
  if (cNeg !== eNeg) return {
    relation:'CONTRADICTED',
    reason:'The claim and excerpt use opposite explicit negation while referring to the same core subject.',
    next:'Check the full source context and look for an independent source addressing the same claim.'
  };
  if (cDir !== 'NONE' && eDir !== 'NONE' && cDir !== eDir) return {
    relation:'CONTRADICTED',
    reason:'The claim and excerpt point in opposite directions for the same outcome.',
    next:'Verify the measurement, time period, and source context before drawing a conclusion.'
  };
  return {
    relation:'SUPPORTED',
    reason:'The excerpt directly overlaps with the claim and does not contain an opposing direction or explicit negation.',
    next:'Check source authority and seek a second independent source before treating the claim as well-supported.'
  };
}
