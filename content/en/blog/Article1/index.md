---
title: "Never Miss a Paper Again: PubMed/Scopus RSS → Telegram in 10 Minutes"
date: 2025-08-16T17:15:29+03:00
draft: false
translationKey: "1755353729-Never Miss a Paper Again: PubMed-Scopus RSS → Telegram in 10 Minutes"
description: A practical, copy-and-paste guide for researchers who want new papers to come to them—in an RSS reader or straight into a Telegram channel/group.
summary: ""
tags:
  - rss
  - ClinicalResearch
  - PubMed
  - Scopus
  - Journals
  - Telegram
  - LifeHacks
categories: 
series: 
showToc: true
TocOpen: false
ShowBreadCrumbs: true
ShowPostNavLinks: false
ShowReadingTime: true
ShowShareButtons: true
ShowWordCount: false
comments: false
hidemeta: false
disableShare: false
cover:
  image: group_12552.webp
  alt: ""
  caption: ""
  relative: true
math: false
mermaid: true
canonicalURL: ""
aliases: 
weight: 1
---

## Why RSS still rocks for researchers
RSS (Really Simple Syndication) is a stream of updates from a source (journal, search, author, etc.). Subscribe once, and new items land in your reader—or your Telegram channel—without refreshing 20 tabs. It’s fast, lightweight, and works across most scholarly sites.

![Pastedimage20250816184034.png](/Pastedimage20250816184034.png)

## What you’ll need

- **One place to receive updates:**
    
    - An **RSS reader** (e.g. Inoreader, Feedly, NewsBlur, NetNewsWire, Reeder).
        
    - **OR** a **Telegram setup** (Feed Reader Bot / RSS bot) to push updates to a **channel** (broadcast) or **group** (team discussion).
        
- **Your sources:** PubMed searches, Scopus searches or author/document pages.
## PubMed: turn any search into an RSS feed 

1. **Run your PubMed search** and apply filters (Trials only, Reviews, Most Recent, date ranges, article types, language, etc.).
    
2. Click **Create RSS** right under the search box.
    
3. Name the feed, then **Create RSS**.
    
4. Copy the **RSS Feed Link**.
![Pasted image 20250816184853.png](/Pastedimage20250816184853.png)



### For Scopus, Web of science or the rest of the databases
mostly I will do the same steps we did in PubMed and you will see the RSS feed sign in the page of search

---

## Journals & sites without an obvious feed

- Many journals expose **Latest/Early View/In Press** feeds—look for the orange RSS icon or “RSS/XML” in the footer.
		Here an example from [JAMA Network](https://jamanetwork.com/)
		- ![Pasted image 20250816185412.png](/Pastedimage20250816185412.png)
		- ![Pasted image 20250816185432.png|355](/Pastedimage20250816185432.png)
    
- If a site has no feed, generate one with [**RSSHub** Radar (open-source) Chrome extension](https://chromewebstore.google.com/detail/rsshub-radar/kefjpfngnndepjbopdmoebkipbgkggaa)
    

---

## Where to read: two winning patterns

### 1) A classic RSS reader 

Use [Inoreader](https://www.inoreader.com/)/[Feedly](https://feedly.com/): paste the feed URL 
![Pasted image 20250816185939.png](/Pastedimage20250816185939.png)
![Pasted image 20250816190004.png](/Pastedimage20250816190004.png)
### 2) Telegram (for teams, or personal push)

**[RSS Bot ](https://t.me/rss2tg_bot)(@rss2tg_bot)**
  
- To post into a **Channel** or **Group**:
    
    1. Add the bot as **Admin** of the channel/group.
        
    2. In the bot: `/channel` (or `/group`) → select your destination → then `/add <feed_url>`.
        
        ![Pasted image 20250816190347.png|280](/Pastedimage20250816190347.png) 
        ![Pasted image 20250816190436.png|252](/Pastedimage20250816190436.png)
        ![Pasted image 20250816190456.png|219](/Pastedimage20250816190456.png)
        ![Pasted image 20250816191342.png](/Pastedimage20250816191342.png)
        added the two feeds from my blog in the channel by writeing this code 
	        `@rss2tg_bot https://<RSSfeed LINK You Copied from the Source>`
        to adjust the settings you have to write this code 
        `/settings@rss2tg_bot`
