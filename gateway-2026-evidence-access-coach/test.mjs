import assert from 'node:assert/strict';
import {assessEvidence} from './app.mjs';
const cases = [
  ['support','School garden reduced cafeteria food waste','School garden project reduced cafeteria food waste by 18 percent','SUPPORTED'],
  ['contradict-negation','School garden reduced cafeteria food waste','The school garden did not reduce cafeteria food waste','CONTRADICTED'],
  ['insufficient','School garden reduced cafeteria food waste','Students reported liking outdoor classes','INSUFFICIENT'],
  ['missing','School garden reduced cafeteria food waste','','INSUFFICIENT'],
  ['directional','School garden reduced cafeteria food waste','The school garden decreased cafeteria food waste by 18 percent','SUPPORTED'],
  ['opposite-direction','School garden reduced cafeteria food waste','The school garden increased cafeteria food waste by 18 percent','CONTRADICTED']
];
for (const [name,c,e,expected] of cases) assert.equal(assessEvidence(c,e).relation, expected, name);
console.log(`${cases.length}/${cases.length} PASS`);
