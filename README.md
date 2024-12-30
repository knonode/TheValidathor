# The Validathor
prototype for an on-chain multiplayer validator node simulation game.

## Game Overview
The game consists of transactions (txn) that are minted as non-fungible tokens on Algorand ledger. Each txn is a number on a matrix.

## Game Start
A game round starts with participants purchasing txns, or "Going online". Purchase should be random, either with a shuffle market app or prepaid and randomly distributed to Pera wallet inboxes or NFD vaults.

## Block Creation & Validation
Combining transactions produce a block, which is minted as a new nft. The tokens used to create a block are burned with ARC54.
Participants race to be the first to validate a block and get a reward from a pool. There are many possible combinations, but fewer blocks can actually be validated.

## Current Implementation
In this prototype we are using Pascal's Triangle with binomial coefficients with 77 rows which gives 3003 txns. The txn number consists of a two digit row number and a two digit position number in the row. Ex. - (2305) - row 25, position 5 from the left.

### Block Format
A block is formatted as such: [0x1507170903] where 0x is decoration, 1507 is the first txn, 1709 is the last txn and 03 is the factor 03.

### Validation Rules
A block is valid if:

1. it is built with 3, 7, 11 or 13 txns, which are the prime factors of 3003.
2. the row numbers are sequential. 01, 02, 03 or 03, 02, 01
3. same block has not already been validated. I.e. The block [0x1604180703] is the same as [0x1607180903], but block [0x1507170903] is not, since it is not the same sequence 15-16-17.

## Trading & Censoring
Participants can trade txns on secondary markets.
Participants can censor txns by burning them with ARC54. Burning txns diminishes possible combinations, by which diminishes opponents possibilities to earn rewards.

## Rewards
Reward pool is a share of proceedings from initial txn sales. A share goes to the project team for op costs.
The reward formula for Pascal's Triangle is:

reward = (factor/possible combinations) x reward pool

example of reward for a block with 11 txns in a 77 row triangle with reward pool of 240 Algo:

(11/278) x 240 = 9.5 Algo

The pool and the consequent rewards can be much larger as well, once the costs of building the game has been covered, it should not be very expensive to maintain.

## Game Completion
A game round is finished when no more blocks can be produced. In a Pascal triangle of 77 rows it would be maximum 278 blocks. Participants are left with block rewards, block nfts and the unused txn nfts.

## Future Development
Next round can be constructed with the same construct but different number of rows, or constructs such as Latin squares, binomial distribution grids, latin squares and others can be used. Possibility of reusing txns from previous rounds must be explored.

### User Experience
The game's UX can include automated block building, so that the participants can watch it unfold without much input.

### Bot Mitigation
Regardless of distribution model, there can be custom made block building  bots. In that case the distribution model should be prepaid assets randomized in time and/or amount. That should prohibit bots from having an unfair advantage. Having to purchase missing txns for a wanted block on secondary market could add another threshold for bots and further mitigate their advantage.

## Current Status
As of today The Validathor game exists as a one player prototype in vanilla HTML, CSS and JS. I don't have the skills (yet) create a true web3 game, so if you want to join building I would be very happy. If you'd like to steal the idea and build it, I would only be a little happy.