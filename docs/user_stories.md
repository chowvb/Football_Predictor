# 📖 User Stories — Football Match Prediction App

This document contains the **Product Backlog** for the Football Prediction Application.  
It is organized into **Epics** and **User Stories**, each with acceptance criteria and tasks.  

---

## ✅ Epic 1: Prediction Engine

### Story 1.1 — Input/Output Skeleton
**As a user, I want to enter two team names, so that I can request a prediction.**

- **Acceptance Criteria:**
  - User can call a function `predict_match(home, away)`.
  - System validates team names.
  - System returns placeholder probabilities (e.g., 33/33/33).

- **Tasks:**
  - [x] Create function skeleton.
  - [x] Add team name validation.
  - [x] Return dummy probabilities.

---

### Story 1.2 — Poisson Simulation
**As a user, I want to see probabilistic outcomes using goals modelling, so that results feel realistic.**

- **Acceptance Criteria:**
  - Implement expected goals for each team.
  - Use Poisson distribution to simulate outcomes.
  - Output most likely scoreline with probabilities.

- **Tasks:**
  - [ ] Implement goal expectation calculation.
  - [ ] Integrate Poisson formula.
  - [ ] Output top 3 scorelines.

---

### Story 1.3 — Elo Engine (Static)
**As a user, I want to see team strengths based on Elo ratings, so that predictions reflect quality differences.**

- **Acceptance Criteria:**
  - Load initial Elo ratings from a CSV.
  - Return Elo ratings alongside predictions.
  - Predictions weighted by Elo difference.

- **Tasks:**
  - [ ] Define Elo formula.
  - [ ] Create CSV for initial team ratings.
  - [ ] Integrate Elo into prediction model.

---

### Story 1.4 — Elo Updates (Dynamic)
**As an admin, I want team ratings to change after each match, so that future predictions reflect results.**

- **Acceptance Criteria:**
  - Elo ratings update after every result.
  - Handle win/draw/loss correctly.
  - Save updated Elo ratings back to CSV.

- **Tasks:**
  - [ ] Implement update function.
  - [ ] Apply correct K-factor.
  - [ ] Save updated ratings.

---

### Story 1.5 — Form Factor
**As a fan, I want predictions to include recent form, so that the model captures momentum.**

- **Acceptance Criteria:**
  - System tracks last 5 matches for each team.
  - Form blended with Elo in final prediction.
  - Configurable weight (Elo vs Form).

- **Tasks:**
  - [ ] Store past results in memory/CSV.
  - [ ] Calculate form index (GF/GA).
  - [ ] Adjust prediction weightings.

---

## ✅ Epic 2: Data Management

### Story 2.1 — Persistent Storage
**As a system, I want to persist team ratings, so that predictions are consistent across restarts.**

- **Acceptance Criteria:**
  - Load Elo ratings on startup.
  - Save ratings after each match update.

- **Tasks:**
  - [ ] Define storage schema (CSV/SQLite).
  - [ ] Implement load function.
  - [ ] Implement save function.

---

### Story 2.2 — Fixture Batch Predictions
**As a user, I want to provide multiple fixtures, so that I can get predictions for an entire weekend.**

- **Acceptance Criteria:**
  - System accepts a fixture list.
  - Predictions run for each match.
  - Results shown in a table.

- **Tasks:**
  - [ ] Define fixture input format.
  - [ ] Implement batch loop.
  - [ ] Output formatted results.

---

### Story 2.3 — Results Entry
**As an admin, I want to enter match results, so that Elo updates automatically.**

- **Acceptance Criteria:**
  - Results accepted in bulk or interactively.
  - Elo updates applied correctly.
  - Updated ratings saved.

- **Tasks:**
  - [ ] Create result input parser.
  - [ ] Validate scores.
  - [ ] Update ratings.

---

### Story 2.4 — Historical Accuracy Tracking
**As an analyst, I want to track prediction accuracy, so that I can improve the model.**

- **Acceptance Criteria:**
  - Save predicted vs actual results.
  - Compute accuracy metrics (e.g., Brier score).
  - Generate summary report.

- **Tasks:**
  - [ ] Save predictions + results to file.
  - [ ] Implement accuracy calculation.
  - [ ] Create reporting function.

---

## ✅ Epic 3: User Interface

### Story 3.1 — CLI Predictions
**As a user, I want to run predictions from the terminal, so that I can interact quickly.**

- **Tasks:**
  - [ ] Command-line input for fixtures.
  - [ ] Text output of probabilities.

---

### Story 3.2 — CLI Results Entry
**As an admin, I want to type results into the terminal, so that ratings update without editing files.**

- **Tasks:**
  - [ ] Prompt user for results.
  - [ ] Parse and validate input.
  - [ ] Update Elo ratings.

---

### Story 3.3 — Web Dashboard (Basic)
**As a fan, I want to view predictions on a web page, so that it’s more user-friendly.**

- **Tasks:**
  - [ ] Build Flask/FastAPI endpoint.
  - [ ] Serve HTML table of predictions.

---

### Story 3.4 — Web Dashboard (Visual)
**As a fan, I want to see probability charts, so that I can visualize outcomes.**

- **Tasks:**
  - [ ] Add W/D/L pie chart.
  - [ ] Add scoreline distribution bar chart.

---

## ✅ Epic 4: Automation

### Story 4.1 — Auto Fixture Fetch
**As a user, I want fixtures pulled from an API, so that I don’t need to enter them manually.**

- **Tasks:**
  - [ ] Connect to fixture API.
  - [ ] Parse data into fixture list.
  - [ ] Run batch predictions.

---

### Story 4.2 — Scheduled Runs
**As a user, I want predictions to auto-generate weekly, so that I don’t have to run them manually.**

- **Tasks:**
  - [ ] Add cron job / task scheduler.
  - [ ] Save weekly predictions to file.

---

## ✅ Epic 5: Advanced Features (Stretch Goals)

- Story 5.1: Betting odds comparison  
- Story 5.2: Multi-league support  
- Story 5.3: Machine learning enhancement  

*(Details to be refined once core system is stable.)*  

---

# 🗂 Workflow

- **Backlog:** Stories not yet started.  
- **In Progress:** Stories under development.  
- **Done:** Completed and tested stories.  

We track **active sprint stories** in GitHub Issues for easier Kanban management.  
This file (`user_stories.md`) acts as the **master backlog**.

