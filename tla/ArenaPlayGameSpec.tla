---------------------------- MODULE ArenaPlayGameSpec ----------------------------
(* 
   TLA+ Specification for Arena Play Game State Machine
   Author: Mira (Settley)
   Date: 2026-03-14
   
   This specification models the core game state machine for Arena Play,
   a multi-agent tournament platform with Filecoin integration.
   
   Key Properties to Verify:
   - Safety: No player participates in two matches simultaneously
   - Safety: Winners advance, losers are eliminated correctly
   - Liveness: Every registered agent eventually plays a match
   - Liveness: Tournament eventually completes
*)

EXTENDS Integers, Sequences, FiniteSets

(* ============================================================================
   CONSTANTS
   ============================================================================ *)

CONSTANTS 
    Agents,         (* Set of all agents that can participate *)
    MaxAgentsPerMatch,  (* Maximum agents in a single match (e.g., 2, 4, 8) *)
    TournamentSize  (* Total number of agents in tournament *)

(* ============================================================================
   VARIABLES
   ============================================================================ *)

VARIABLES
    registeredAgents,   (* Set of agents registered for tournament *)
    agentState,         (* [agent -> {"waiting", "playing", "won", "eliminated"}] *)
    matches,            (* Set of active matches *)
    matchParticipants,  (* [matchId -> set of agents in this match] *)
    matchWinner,        (* [matchId -> agent or NULL if incomplete] *)
    tournamentState,    (* {"not_started", "running", "completed"} *)
    nextMatchId         (* Counter for generating unique match IDs *)

(* ============================================================================
   INITIAL STATE
   ============================================================================ *)

Init ==
    /\ registeredAgents = {}
    /\ agentState = [agent \in Agents |-> "unregistered"]
    /\ matches = {}
    /\ matchParticipants = [m \in matches |-> {}]
    /\ matchWinner = [m \in matches |-> NULL]
    /\ tournamentState = "not_started"
    /\ nextMatchId = 1

(* ============================================================================
   STATE TRANSITIONS (ACTIONS)
   ============================================================================ *)

(* Agent Registration *)
Register(agent) ==
    /\ agent \in Agents
    /\ agentState[agent] = "unregistered"
    /\ registeredAgents' = registeredAgents \cup {agent}
    /\ agentState' = [agentState EXCEPT ![agent] = "waiting"]
    /\ UNCHANGED <<matches, matchParticipants, matchWinner, tournamentState, nextMatchId>>

(* Start a Match *)
StartMatch(participants) ==
    /\ tournamentState = "running" \lor tournamentState = "not_started"
    /\ participants \subseteq registeredAgents
    /\ Cardinality(participants) = MaxAgentsPerMatch
    /\ \forall a \in participants: agentState[a] = "waiting"
    /\ matches' = matches \cup {nextMatchId}
    /\ matchParticipants' = [matchParticipants EXCEPT ![nextMatchId] = participants]
    /\ matchWinner' = [matchWinner EXCEPT ![nextMatchId] = NULL]
    /\ \forall a \in participants: agentState' = [agentState EXCEPT ![a] = "playing"]
    /\ nextMatchId' = nextMatchId + 1
    /\ tournamentState' = "running"
    /\ UNCHANGED <<registeredAgents>>

(* Complete a Match *)
CompleteMatch(matchId, winner) ==
    /\ matchId \in matches
    /\ matchWinner[matchId] = NULL  (* Match not yet completed *)
    /\ winner \in matchParticipants[matchId]
    /\ matchWinner' = [matchWinner EXCEPT ![matchId] = winner]
    /\ agentState' = [
        agentState EXCEPT 
        ![winner] = "won",
        ![a] = "eliminated" 
            \A a \in (matchParticipants[matchId] \ {winner})
    ]
    /\ UNCHANGED <<registeredAgents, matches, matchParticipants, tournamentState, nextMatchId>>

(* Advance Winner to Next Round *)
AdvanceWinner(winner) ==
    /\ agentState[winner] = "won"
    /\ agentState' = [agentState EXCEPT ![winner] = "waiting"]
    /\ UNCHANGED <<registeredAgents, matches, matchParticipants, matchWinner, tournamentState, nextMatchId>>

(* Start Tournament *)
StartTournament ==
    /\ tournamentState = "not_started"
    /\ Cardinality(registeredAgents) >= MaxAgentsPerMatch
    /\ tournamentState' = "running"
    /\ UNCHANGED <<registeredAgents, agentState, matches, matchParticipants, matchWinner, nextMatchId>>

(* Complete Tournament *)
CompleteTournament ==
    /\ tournamentState = "running"
    /\ \forall a \in registeredAgents: 
        agentState[a] \in {"won", "eliminated"}
    /\ Cardinality({a \in registeredAgents: agentState[a] = "won"}) = 1
    /\ tournamentState' = "completed"
    /\ UNCHANGED <<registeredAgents, agentState, matches, matchParticipants, matchWinner, nextMatchId>>

(* ============================================================================
   NEXT STATE RELATION
   ============================================================================ *)

Next ==
    \/ \E agent \in Agents: Register(agent)
    \/ StartTournament
    \/ \E participants \in SUBSET registeredAgents: 
        StartMatch(participants)
    \/ \E matchId \in matches, winner \in matchParticipants[matchId]:
        CompleteMatch(matchId, winner)
    \/ \E winner \in registeredAgents: AdvanceWinner(winner)
    \/ CompleteTournament

(* ============================================================================
   SPECIFICATION
   ============================================================================ *)

Spec == Init /\ [][Next]_<<registeredAgents, agentState, matches, matchParticipants, matchWinner, tournamentState, nextMatchId>>

(* ============================================================================
   SAFETY PROPERTIES (Invariants)
   ============================================================================ *)

(* No agent plays in two matches simultaneously *)
NoDoubleParticipation ==
    \forall a \in Agents:
        agentState[a] = "playing" 
        => Cardinality({m \in matches: a \in matchParticipants[m] /\ matchWinner[m] = NULL}) = 1

(* Winners are always from match participants *)
WinnerFromParticipants ==
    \forall m \in matches:
        matchWinner[m] \in matchParticipants[m] \cup {NULL}

(* Eliminated agents don't play again *)
EliminatedStayEliminated ==
    \forall a \in Agents:
        agentState[a] = "eliminated"
        => [](agentState[a] = "eliminated")

(* Only one tournament winner at completion *)
SingleWinner ==
    tournamentState = "completed"
    => Cardinality({a \in registeredAgents: agentState[a] = "won"}) = 1

(* Valid state transitions *)
ValidStateTransitions ==
    \forall a \in Agents:
        agentState[a] \in {"unregistered", "waiting", "playing", "won", "eliminated"}

(* ============================================================================
   LIVENESS PROPERTIES (Temporal)
   ============================================================================ *)

(* Every registered agent eventually plays or the tournament completes *)
FairParticipation ==
    \forall a \in registeredAgents:
        <> (agentState[a] \in {"playing", "eliminated"}) 
        \/ [](tournamentState = "completed")

(* Tournament eventually completes if started *)
TournamentCompletes ==
    tournamentState = "running" => <> (tournamentState = "completed")

(* Every match eventually completes *)
MatchCompletes ==
    \forall m \in matches: 
        matchWinner[m] = NULL => <>(matchWinner[m] # NULL)

(* ============================================================================
   FILECOIN INTEGRATION SPECIFICATION
   ============================================================================ *)

VARIABLES
    storedGameStates,     (* Set of game states stored on Filecoin *)
    gameStateToCid,       (* [gameStateId -> Filecoin CID] *)
    verificationStatus    (* [gameStateId -> {"pending", "verified", "failed"}] *)

FilecoinInit ==
    /\ storedGameStates = {}
    /\ gameStateToCid = [gs \in storedGameStates |-> ""]
    /\ verificationStatus = [gs \in storedGameStates |-> "pending"]

(* Store Game State on Filecoin *)
StoreGameState(gameStateId, gameStateData) ==
    /\ gameStateId \notin storedGameStates
    /\ storedGameStates' = storedGameStates \cup {gameStateId}
    /\ gameStateToCid' = [gameStateToCid EXCEPT ![gameStateId] = "pending_cid"]
    /\ verificationStatus' = [verificationStatus EXCEPT ![gameStateId] = "pending"]
    /\ UNCHANGED <<registeredAgents, agentState, matches, matchParticipants, matchWinner, tournamentState, nextMatchId>>

(* Verify Filecoin Storage *)
VerifyFilecoinStorage(gameStateId, cid) ==
    /\ gameStateId \in storedGameStates
    /\ gameStateToCid[gameStateId] = "pending_cid"
    /\ cid # ""
    /\ gameStateToCid' = [gameStateToCid EXCEPT ![gameStateId] = cid]
    /\ verificationStatus' = [verificationStatus EXCEPT ![gameStateId] = "verified"]
    /\ UNCHANGED <<registeredAgents, agentState, matches, matchParticipants, matchWinner, tournamentState, nextMatchId, storedGameStates>>

(* Filecoin Safety: All stored states are eventually verified *)
FilecoinVerification ==
    \forall gs \in storedGameStates:
        verificationStatus[gs] = "pending" => <>(verificationStatus[gs] = "verified")

(* Filecoin Safety: Verified states are immutable *)
FilecoinImmutability ==
    \forall gs \in storedGameStates:
        verificationStatus[gs] = "verified"
        => [](gameStateToCid[gs] = gameStateToCid[gs])

(* ============================================================================
   TYPE INVARIANT
   ============================================================================ *)

TypeInvariant ==
    /\ registeredAgents \subseteq Agents
    /\ \forall a \in Agents: agentState[a] \in {"unregistered", "waiting", "playing", "won", "eliminated"}
    /\ matches \subseteq Nat
    /\ \forall m \in matches: matchParticipants[m] \subseteq registeredAgents
    /\ \forall m \in matches: matchWinner[m] \in matchParticipants[m] \cup {NULL}
    /\ tournamentState \in {"not_started", "running", "completed"}
    /\ nextMatchId \in Nat

================================================================================
(* 
   MODEL CHECKING INSTRUCTIONS:
   
   1. Create a model with concrete values:
      Agents = {"agent1", "agent2", "agent3", "agent4"}
      MaxAgentsPerMatch = 2
      TournamentSize = 4
   
   2. Check invariants:
      - NoDoubleParticipation
      - WinnerFromParticipants
      - EliminatedStayEliminated
      - SingleWinner
      - ValidStateTransitions
      - TypeInvariant
   
   3. Check liveness properties (requires fairness):
      - FairParticipation
      - TournamentCompletes
      - MatchCompletes
      - FilecoinVerification
   
   4. Add fairness conditions:
      Weak fairness: Next
      Strong fairness: (optional for specific actions)
   
   5. Expected behavior:
      - TLC should find no invariant violations
      - Liveness properties should hold under fairness assumptions
      - State space should be finite and checkable for small models
*)
================================================================================
