# TLA+ Specifications for Arena Play

Formal specifications for verifying Arena Play's distributed multi-agent tournament system.

## Files

- **ArenaPlayGameSpec.tla** - Core game state machine specification
  - Agent registration and tournament lifecycle
  - Match creation, completion, and winner advancement
  - Safety invariants (no double participation, single winner, etc.)
  - Liveness properties (tournament completion, fair participation)
  - Filecoin integration for immutable game state storage

## Verification Goals

### Safety Properties (Nothing bad happens)
- ✅ No agent participates in two matches simultaneously
- ✅ Tournament winners are always actual match participants
- ✅ Eliminated agents don't play again
- ✅ Exactly one tournament winner at completion
- ✅ All game states stored on Filecoin are eventually verified
- ✅ Verified Filecoin CIDs are immutable

### Liveness Properties (Something good eventually happens)
- ✅ Every registered agent eventually plays or tournament completes
- ✅ Tournament eventually completes if started
- ✅ Every match eventually completes
- ✅ Filecoin storage is eventually verified

## Model Checking

### Prerequisites
1. Install [TLA+ Toolbox](https://github.com/tlaplus/tlaplus/releases)
2. Or use command-line TLC model checker

### Running Verification

1. Open `ArenaPlayGameSpec.tla` in TLA+ Toolbox
2. Create a new model with these parameters:
   ```
   Agents = {"agent1", "agent2", "agent3", "agent4"}
   MaxAgentsPerMatch = 2
   TournamentSize = 4
   ```
3. Add invariants to check:
   - `NoDoubleParticipation`
   - `WinnerFromParticipants`
   - `EliminatedStayEliminated`
   - `SingleWinner`
   - `ValidStateTransitions`
   - `TypeInvariant`
4. Add temporal properties (requires fairness):
   - `TournamentCompletes`
   - `MatchCompletes`
   - `FilecoinVerification`
5. Set fairness: Weak fairness on `Next` action
6. Run TLC model checker

### Expected Results
- No invariant violations
- Liveness properties hold under fairness assumptions
- State space: ~thousands of states for 4-agent model

## Learning Resources

- [TLA+ Video Course](https://lamport.azurewebsites.net/video/videos.html) - Leslie Lamport's official course
- [Specifying Systems](https://www.microsoft.com/en-us/research/uploads/prod/2018/05/book-02-08-08.pdf) - Free book by Lamport
- [Awesome TLA+](https://github.com/tlaplus/awesome-tlaplus) - Curated resources

## Next Steps

1. ✅ Core game state machine (completed)
2. ⏳ Tournament bracket management (pending)
3. ⏳ Consensus protocol for match outcomes (pending)
4. ⏳ Filecoin storage verification protocol (pending)
5. ⏳ Agent swarm coordination spec (pending)

## Notes

- This specification uses standard TLA+ notation
- Filecoin integration ensures immutable game state audit trail
- Model checking catches subtle concurrency bugs before implementation
- Start with small models (4 agents) then scale up
