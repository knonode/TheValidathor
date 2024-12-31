# The Validathor
A prototype for an on-chain multiplayer validator node simulation game.

## Game Overview
The game consists of transactions (txn) that are minted as non-fungible tokens on the Algorand ledger. Each txn represents a number on a matrix. The matrix represents a ledger out of consensus. A bug has forked the chain 77 times. We need healthy nodes to bring the ledger back on track. Who will make the one true chain? Who will be .... The Validathor!!!
'cue metal guitar riff'

## Game Start
A game round starts with participants purchasing txns, or "Going online". Purchases should be random, either through a shuffle market app or prepaid and randomly distributed to Pera wallet inboxes or NFD vaults.

## Block Creation & Validation
Combining transactions produces a block, which is minted as a new NFT. The tokens used to create a block are burned using ARC54.
Participants race to be the first to validate a block and get a reward from a pool. There are many possible combinations, but only a limited number of blocks can actually be validated.

## Current Implementation
In this prototype, we are using Pascal's Triangle with binomial coefficients with 77 rows, which gives 3003 txns. Each txn number consists of a two-digit row number and a two-digit position number in the row. Example: (2305) - row 23, position 05 from the left.

### Block Format
A block is formatted as: [0x1507170903] where 0x is decoration, 1507 is the first txn, 1709 is the last txn, and 03 is the factor 03.

### Validation Rules
A block is valid if:

1. It is built with 3, 7, 11, or 13 txns, which are the prime factors of 3003.
2. The row numbers are sequential (e.g., 01, 02, 03 or 03, 02, 01).
3. The same block has not already been validated. For example, block [0x1604180703] is the same as [0x1607180903], but block [0x1507170903] is different since it's not the same sequence 15-16-17.

## Trading & Censoring
Participants can trade txns on secondary markets.
Participants can censor txns by burning them with ARC54. Burning txns reduces possible combinations, which in turn reduces opponents' possibilities to earn rewards.

## Rewards
The reward pool is a share of proceeds from initial txn sales. A share goes to the project team for operational costs.
The reward formula for Pascal's Triangle is:

reward = (factor/possible combinations) x reward pool

Example of a reward for a block with 11 txns in a 77-row triangle with a reward pool of 240 Algo:

(11/278) x 240 = 9.5 Algo

The pool and the consequent rewards can be much larger. Once the costs of building the game have been covered, it should not be very expensive to maintain.

## Game Completion
A game round is finished when no more blocks can be produced. In a Pascal triangle of 77 rows, there would be a maximum of 278 blocks. Participants are left with block rewards, block NFTs, and unused txn NFTs.

## Future Development
The next round can be constructed with the same structure but different number of rows, or other constructs such as Latin squares, binomial distribution grids, and other mathematical patterns can be used. The possibility of reusing txns from previous rounds must be explored. The game's UX can include automated block building, allowing participants to watch it unfold without much input.

## Bot Mitigation
While custom-made block-building bots are possible regardless of the distribution model, using prepaid assets randomized in time and/or amount should help mitigate their advantage. Having to purchase missing txns for a wanted block on the secondary market could add another threshold for bots and further reduce their advantage.

## Current Status
Currently, The Validathor exists as a one-player prototype in vanilla HTML, CSS, and JS. I don't have the skills (yet) to create a true web3 game, so if you want to join in building it, I would be very happy. If you'd like to steal the idea, I would only be a little happy.