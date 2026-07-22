# Project Tickets: SQL ReAct Agent using LangChain + LangGraph

## Objective

Build a production-style SQL ReAct Agent incrementally using LangChain
for tool calling and LangGraph for orchestration.

------------------------------------------------------------------------

# Sprint 1 -- Foundation

## TICKET-001: Project Setup

**Description** - Create project structure - Create virtual
environment - Install: - langchain - langgraph - langchain-openai -
python-dotenv - mysql-connector-python - Configure `.env` - Verify LLM
connection

**Acceptance Criteria** - `main.py` runs successfully. - LLM returns a
response.

------------------------------------------------------------------------

## TICKET-002: SQL Tool

**Description** - Convert `query_executor` into a LangChain `@tool`.

**Acceptance Criteria** - `query_executor.invoke()` executes SQL
successfully.

------------------------------------------------------------------------

## TICKET-003: Human Input Tool

**Description** - Convert `take_user_input` into a LangChain `@tool`.

**Acceptance Criteria** - Tool returns user input correctly.

------------------------------------------------------------------------

## TICKET-004: Tool Validation

**Description** - Test every tool independently.

**Acceptance Criteria** - All tools work without an agent.

------------------------------------------------------------------------

# Sprint 2 -- LangChain ReAct

## TICKET-005: Bind Tools

**Description** - Bind all tools using `llm.bind_tools()`.

**Acceptance Criteria** - LLM produces structured tool calls.

------------------------------------------------------------------------

## TICKET-006: Manual ReAct Loop

**Description** - Implement a ReAct loop using LangChain tool calling.

**Acceptance Criteria** - Agent answers SQL questions correctly.

------------------------------------------------------------------------

## TICKET-007: Error Handling

**Description** - Handle invalid SQL, empty results, and database
failures.

**Acceptance Criteria** - Agent fails gracefully without crashing.

------------------------------------------------------------------------

# Sprint 3 -- LangGraph

## TICKET-008: Define State

**Description** - Create the LangGraph state.

**Acceptance Criteria** - Graph compiles successfully.

------------------------------------------------------------------------

## TICKET-009: Chatbot Node

**Description** - Implement the LLM node.

**Acceptance Criteria** - Returns an AI message.

------------------------------------------------------------------------

## TICKET-010: Tool Node

**Description** - Implement `ToolNode`.

**Acceptance Criteria** - Tools execute correctly inside the graph.

------------------------------------------------------------------------

## TICKET-011: Conditional Routing

**Description** - Route between Chatbot, ToolNode, and END.

**Acceptance Criteria** - Graph loops until completion.

------------------------------------------------------------------------

## TICKET-012: Complete Graph

**Architecture**

``` text
START
  |
Chatbot
  |
Need Tool?
 |      |
Yes     No
 |       |
Tool    END
 |
Chatbot
```

**Acceptance Criteria** - Complete SQL ReAct Agent works end-to-end.

------------------------------------------------------------------------

# Sprint 4 -- Memory

## TICKET-013: Checkpointing

-   Add `MemorySaver`.
-   Persist conversations.

## TICKET-014: Multi-turn Conversation

-   Verify conversation history across multiple user turns.

------------------------------------------------------------------------

# Sprint 5 -- Human-in-the-Loop

## TICKET-015: Interrupts

-   Replace input tool with LangGraph interrupts.

**Acceptance Criteria** - Graph pauses and resumes correctly.

------------------------------------------------------------------------

# Sprint 6 -- Production

## TICKET-016: Production Readiness

Add: - Logging - Retry mechanism - Streaming - Configuration
management - Unit tests

**Acceptance Criteria** - Project is production-ready.

------------------------------------------------------------------------

# Stretch Goals

-   RAG Tool
-   Web Search Tool
-   Multiple Database Support
-   Supervisor Agent
-   SQL Validation Agent
-   SQL Explanation Before Execution
-   Persistent Database-backed Memory
