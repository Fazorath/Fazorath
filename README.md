# Hey, I'm Yoenis 👋

**CS student @ FIU · Software Engineer — full-stack and infrastructure**

I build software that people actually use, and then I have to keep it running. Most of
what I know came from that second part.

### What I'm working on

- **Atlas** *(Python, Docker Compose, PostgreSQL, YAML)* — a self-hosted personal dashboard
  that pulls weather, money, school, sleep, habits, listening and work shifts onto one page
  of widgets you arrange yourself. Each source is a module switched on in one config file,
  and the whole thing comes up with a single `docker compose up`. Has its own
  [manual site](https://fazorath.github.io/atlas-dashboard/).
  [Repo](https://github.com/Fazorath/atlas-dashboard)
- **Overnight** *(Python, Claude Code, git worktrees)* — an agent pipeline I run on my own
  server. During the day I write a spec and break it into tickets; overnight an Opus
  "boss" hands each ticket to a Sonnet worker, a separate reviewer grades every PR against
  its acceptance criteria, and everything lands as a **draft PR** with a morning dashboard.
  Nothing merges without me, and hard usage caps and a guard hook keep it contained.
- **La Tienda scheduling & price app** *(Swift, SwiftUI, PostgreSQL)* — replaced a paper
  schedule and a memorized store-wide price list at a local grocery. In daily use by all
  14 staff; saves the owner ~3 hours a week and the team ~3 hours a day.
  [Repo](https://github.com/Fazorath/la-tienda)
- **Arcanum** *(Linux, Docker Compose, Tailscale, Cloudflare)* — a self-hosted server
  running 15+ containerized services, with remote access engineered around CGNAT and an
  automated update pipeline that won't touch stateful databases unattended.
  [Docs](https://github.com/Fazorath/arcanum-homelab)
- **Paranoid-Jarvis** *(Python, macOS Launch Agent)* — a login watchdog for my Mac: snaps
  a photo from the camera at every login and logs wake, lock-screen and unlock events.
  Everything stays on the machine. [Repo](https://github.com/Fazorath/Paranoid-Jarvis)
- **AbyssTracker** *(Python)* — a desktop app for EVE Online pilots that logs Abyssal and
  Incursion runs and tracks profit, ISK/hour and time per session, with history charts and
  a pocket-mode timer window. [Repo](https://github.com/Fazorath/AbyssTracker)
- **LocalMUD** *(Python)* — a text-based RPG engine: rooms, NPCs, dialogue trees,
  factions, quests, an arena with betting and duels. ~3k lines, JSON-driven content.
  [Repo](https://github.com/Fazorath/LocalMUD)
- **Apartment Dashboard** *(React, Node, Express, MongoDB)* — collaborative chore and
  recurring-task manager for shared living spaces.
  [Repo](https://github.com/Fazorath/Apartment-Dashboard)

Smaller tools: **DevWatch**, a local dashboard for listening ports and dev servers;
[**MacOS-Shutdown-Utility**](https://github.com/Fazorath/MacOS-Shutdown-Utility), exact-time
shutdowns from Shortcuts or the terminal; and a shared Claude Code config that keeps my
homelab, PC and MacBook set up identically.

### Tech I use

`Python` · `JavaScript` · `Swift` · `SwiftUI` · `React Native` · `React` · `Node.js`
`PostgreSQL` · `Supabase` · `MongoDB` · `Linux` · `Docker` · `Tailscale` · `Git`
`Claude Code` (agent workflows and automation)

### What I'm good at

- **Shipping to non-technical users** — every app here was built for people who didn't ask
  for software, they asked for their day to be easier.
- **Running what I build** — container orchestration, networking under real constraints,
  and debugging the failures that only show up in production.
- **Automating the boring parts** — agent pipelines with guardrails, scheduled jobs and
  config that syncs across machines, built so a human still reviews and merges.
- **Data modeling** — relational schemas, REST APIs, role-based access control.

### Find me

[LinkedIn](https://www.linkedin.com/in/yoenis-hernandez) · [Email](mailto:hernandezyoenis@gmail.com)

---

### GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Fazorath&show_icons=true&rank_icon=github)
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Fazorath&layout=compact&hide=html,css)
