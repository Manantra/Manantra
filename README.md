<p align="center">
  <img src="assets/header.svg" alt="Daniel / Manantra — AI, automation and open source" width="100%" />
</p>

<div align="center">

**Educator by profession. Builder by curiosity.**

I build practical tools, untangle complicated systems, and contribute to open source.

[![Projects](https://img.shields.io/badge/Explore_projects-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Manantra?tab=repositories)
[![Contributions](https://img.shields.io/badge/Upstream_PRs-0969DA?style=flat-square&logo=github&logoColor=white)](https://github.com/pulls?q=is%3Apr+author%3AManantra)

</div>

## 👋 Hi, I'm Daniel

I work in **education and school social work** in Germany. Outside of that, I enjoy building software that solves everyday problems — especially where **AI, Home Assistant, automation, and self-hosted tools** meet.

My favorite projects make complex systems **easier to understand**, repetitive work **less tedious**, and technology **more useful without taking control away from its users**. I build my own tools, but I also enjoy making the open-source projects I use a little better.

## 🚀 Featured projects

These are projects and research efforts I maintain under **Manantra** — not just forks of someone else's code.

### 🏠 [HA Lens](https://github.com/Manantra/ha-lens) · Home Assistant automation insights

**See what an automation does, why it runs, and which path it takes.**

A read-only visualizer and analyzer that turns Home Assistant automation YAML into understandable flow graphs, possible execution paths, entity references, and diagnostic insights. Its Home Assistant companion can also display the latest execution trace — **without changing or executing automations**.

`TypeScript` · `React` · `Home Assistant` · `YAML analysis`

### 🧠 [CortexGate](https://github.com/Manantra/cortexgate) · AI content, with a human checkpoint

A mobile-friendly dashboard for reviewing and curating **AI-generated summaries** before saving them to an **Obsidian** knowledge base. Built around a simple idea: automate the collection, keep a person in charge of what gets saved.

`JavaScript` · `PWA` · `Obsidian` · `OpenClaw`

### 🔬 [Echo Dot / Crumpet Research](https://github.com/Manantra/echo-dot-crumpet-research) · Evidence-led reverse engineering

Public, **read-only research** into the Echo Dot 3rd Gen Refresh (Crumpet): firmware structure, boot-chain behavior, and hardware-specific constraints. The documentation distinguishes **verified findings from hypotheses**; it does not claim an established unlock or root method.

`Python` · `Firmware research` · `Documentation`

### ☀️ Smaller tools for everyday workflows

- **[Morning Dashboard](https://github.com/Manantra/morning-dashboard)** — an OpenClaw skill that combines weather, calendar events, tasks, and birthdays into a daily briefing.
- **[People CRM](https://github.com/Manantra/people-crm)** — an OpenClaw skill for organizing personal contacts, relationships, notes, and birthdays.

## 🤝 Open-source contributions

One of my favorite parts of building is contributing improvements **back to the original projects**. Below are selected upstream pull requests, with merged contributions and other proposals distinguished.

### 🌙 [Moonfin](https://github.com/Moonfin-Client/Roku) · Roku client for Jellyfin & Emby

**Selected merged pull requests** across server compatibility, playback, and multi-server behavior:

| Area | Merged contributions |
| :-- | :-- |
| **Emby support** | [Server integration, Connect login, and playback compatibility · #277](https://github.com/Moonfin-Client/Roku/pull/277) |
| **Jellyfin & playback** | [Music routes and remote trailers · #281](https://github.com/Moonfin-Client/Roku/pull/281), [series/season resume · #282](https://github.com/Moonfin-Client/Roku/pull/282), [Live TV remux retries · #283](https://github.com/Moonfin-Client/Roku/pull/283) |
| **Correct server context** | [Video playback · #284](https://github.com/Moonfin-Client/Roku/pull/284), [audio playback · #285](https://github.com/Moonfin-Client/Roku/pull/285), [detail actions · #286](https://github.com/Moonfin-Client/Roku/pull/286) |

*Also submitted:* [Windows-root-path handling for Seerr · #301](https://github.com/Moonfin-Client/Roku/pull/301) and a [season-display toggle · #302](https://github.com/Moonfin-Client/Roku/pull/302).

### 🧠 [claude-mem](https://github.com/thedotmack/claude-mem) · Installer and OpenClaw compatibility

**Merged pull requests** helping keep integrations reliable:

- [Preserve `openclaw.extensions` during installation · #1113](https://github.com/thedotmack/claude-mem/pull/1113)
- [Use the expected OpenClaw command-handler response · #1115](https://github.com/thedotmack/claude-mem/pull/1115)
- [Respect existing installer and plugin-load paths · #1116](https://github.com/thedotmack/claude-mem/pull/1116)

### 🏡 [Parqet Companion](https://github.com/cubinet-code/ha-parqet-companion) · Home Assistant portfolio integration

- **Merged:** [Support multiple Parqet accounts · #7](https://github.com/cubinet-code/ha-parqet-companion/pull/7)
- **Submitted:** [Optimize API requests and cache calendar activity · #10](https://github.com/cubinet-code/ha-parqet-companion/pull/10) and [localize cards in German · #11](https://github.com/cubinet-code/ha-parqet-companion/pull/11)

### 🐒 [NZB Monkey Go](https://github.com/Tensai75/nzb-monkey-go) · macOS compatibility

**Tested on Apple Silicon (M4):** Validated the macOS `nzblnk://` link-handling workflow through to SABnzbd and helped troubleshoot a local-network permission issue.

**Proposed follow-up improvements** in the [discussion of upstream PR #47](https://github.com/Tensai75/nzb-monkey-go/pull/47#issuecomment-6233690040): a macOS Local Network permission description, safer logging to avoid exposing NZBLNK passwords and API keys, an HTTP error regression test, and guidance for preserving configuration during app upgrades.

*Status: Tested locally and shared as an upstream patch; not a separately authored or merged pull request.*

### 🤖 Other upstream proposals

- **[Hermes Agent](https://github.com/NousResearch/hermes-agent):** [Serialize concurrent dependency installs · #84766](https://github.com/NousResearch/hermes-agent/pull/84766) and [scope Kanban tool availability to agent context · #84816](https://github.com/NousResearch/hermes-agent/pull/84816)
- **[Hermex](https://github.com/uzairansaruzi/hermex):** [Display transcript audio as voice bubbles · #44](https://github.com/uzairansaruzi/hermex/pull/44) *(submitted; closed without merge as of October 2026)*

<sub>The hand-picked links above reflect contributions verified in October 2026. The automatically generated section below tracks newly merged PRs.</sub>

## 📡 Latest GitHub activity

<!-- PROFILE_ACTIVITY:START -->
### Recently merged upstream contributions

Automatically gathered from my merged pull requests in other people's repositories.

- **[Moonfin-Client/Roku](https://github.com/Moonfin-Client/Roku)** — [Fix Seerr JSON escaping for Windows root folders · #301](https://github.com/Moonfin-Client/Roku/pull/301) · merged 2026-10-11
- **[Moonfin-Client/Roku](https://github.com/Moonfin-Client/Roku)** — [Keep remote detail actions on the item server · #286](https://github.com/Moonfin-Client/Roku/pull/286) · merged 2026-09-26
- **[Moonfin-Client/Roku](https://github.com/Moonfin-Client/Roku)** — [Fix remote audio playback context · #285](https://github.com/Moonfin-Client/Roku/pull/285) · merged 2026-09-26
- **[cubinet-code/ha-parqet-companion](https://github.com/cubinet-code/ha-parqet-companion)** — [feat: support multiple Parqet accounts · #7](https://github.com/cubinet-code/ha-parqet-companion/pull/7) · merged 2026-07-29
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** — [Respect existing installPath and plugins.load.paths in installer · #1116](https://github.com/thedotmack/claude-mem/pull/1116) · merged 2026-02-16
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** — [Fix installer overwriting package.json and losing openclaw.extensions · #1113](https://github.com/thedotmack/claude-mem/pull/1113) · merged 2026-02-16
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** — [Fix command handlers to return { text } per OpenClaw plugin API · #1115](https://github.com/thedotmack/claude-mem/pull/1115) · merged 2026-02-16

### Recently active original repositories

- **[ha-lens](https://github.com/Manantra/ha-lens)** — Open-source project
- **[echo-dot-crumpet-research](https://github.com/Manantra/echo-dot-crumpet-research)** — Read-only reverse engineering research on Amazon Echo Dot 3rd Gen Refresh \(Crumpet/C78MP8\)
- **[cortexgate](https://github.com/Manantra/cortexgate)** — A lightweight dashboard to review and curate AI-generated content summaries before saving them to your Second Brain \(Obs…
- **[morning-dashboard](https://github.com/Manantra/morning-dashboard)** — OpenClaw Skill: Daily briefing dashboard with weather, calendar, todos, birthdays
- **[people-crm](https://github.com/Manantra/people-crm)** — OpenClaw Skill: Personal CRM for contacts, family, friends, colleagues

<sub>Automated snapshot from the GitHub API. Updates arrive as draft pull requests and are published only after review.</sub>
<!-- PROFILE_ACTIVITY:END -->

<sub>[How this section is updated](docs/AUTOMATION.md) — changes are proposed as draft PRs, never auto-merged.</sub>

## 🧰 Technologies & interests

<p>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/React-149ECA?style=flat-square&logo=react&logoColor=white" alt="React" />
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js" />
  <img src="https://img.shields.io/badge/Home_Assistant-18BCF2?style=flat-square&logo=homeassistant&logoColor=white" alt="Home Assistant" />
  <img src="https://img.shields.io/badge/Obsidian-7C3AED?style=flat-square&logo=obsidian&logoColor=white" alt="Obsidian" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
</p>

**Things I'm drawn to:** smart-home troubleshooting, visual explanations, AI-assisted workflows, knowledge management, local-first software, and useful tools that can be self-hosted.

I also explore and adapt existing software through [forks and experiments](https://github.com/Manantra?tab=repositories). **A fork on its own isn't an upstream contribution** — that's why the section above links to actual pull requests.

## 💡 My approach

> Build useful things. Make them understandable. Keep people in control.

A small, well-documented fix that helps real people can be just as valuable as a big new project.

## ❤️ Support my open-source work

I develop and maintain these projects in my spare time and share them openly. If you find my work useful, you can support ongoing maintenance through GitHub Sponsors. Sponsoring is entirely optional — my open-source projects remain free to use.

[![Sponsor on GitHub](https://img.shields.io/badge/Sponsor_on_GitHub-EA4AAA?style=flat-square&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/Manantra)

---

<p align="center">
  <strong>Thanks for stopping by.</strong><br />
  <a href="https://github.com/Manantra?tab=repositories">Explore my repositories</a> ·
  <a href="https://github.com/pulls?q=is%3Apr+author%3AManantra">Browse my pull requests</a>
</p>
