# prompt_library.py
import json
import os

# ── Build absolute path so it always works ──
BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
DATA_DIR      = os.path.join(BASE_DIR, "..", "data")
LIBRARY_FILE  = os.path.join(DATA_DIR, "prompts_library.json")

DEFAULT_PROMPTS = [
  {
    "id": 1,
    "category": "coding",
    "title": "Debug My Code",
    "prompt": "Review the following code, identify all bugs and errors, explain why each is a problem, and provide the corrected version with detailed inline comments explaining every fix."
  },
  {
    "id": 2,
    "category": "coding",
    "title": "Build REST API",
    "prompt": "Design and build a complete production-ready REST API with proper error handling, JWT authentication, rate limiting, input validation, and full documentation for the following use case:"
  },
  {
    "id": 3,
    "category": "coding",
    "title": "Code Review",
    "prompt": "Perform an expert-level code review. Check for bugs, security vulnerabilities, memory leaks, performance issues, anti-patterns, and suggest refactored improvements with explanations:"
  },
  {
    "id": 4,
    "category": "coding",
    "title": "Optimize Performance",
    "prompt": "Analyze this code for every possible performance bottleneck. Rewrite it using best practices, optimal algorithms, and efficient data structures while maintaining identical functionality:"
  },
  {
    "id": 5,
    "category": "coding",
    "title": "Write Unit Tests",
    "prompt": "Write a comprehensive test suite with unit tests, integration tests, edge cases, error scenarios, and mock setups. Aim for 100% coverage for the following code:"
  },
  {
    "id": 6,
    "category": "coding",
    "title": "System Architecture",
    "prompt": "Design a complete scalable system architecture for the following application. Include database design, API structure, caching strategy, load balancing, and deployment plan:"
  },
  {
    "id": 7,
    "category": "coding",
    "title": "Refactor Legacy Code",
    "prompt": "Refactor the following legacy code into clean, modern, maintainable code following SOLID principles, design patterns, and current best practices:"
  },
  {
    "id": 8,
    "category": "coding",
    "title": "Database Schema",
    "prompt": "Design an optimized relational database schema with proper indexing, foreign keys, constraints, and normalization for the following application:"
  },
  {
    "id": 9,
    "category": "coding",
    "title": "Security Audit",
    "prompt": "Perform a thorough security audit on the following code. Identify all OWASP Top 10 vulnerabilities, injection risks, authentication flaws, and provide hardened fixes:"
  },
  {
    "id": 10,
    "category": "coding",
    "title": "Algorithm Design",
    "prompt": "Design the most efficient algorithm to solve the following problem. Analyze time and space complexity, compare approaches, and implement the optimal solution:"
  },
  {
    "id": 11,
    "category": "coding",
    "title": "Docker Setup",
    "prompt": "Create a complete Docker and Docker Compose setup with multi-stage builds, environment variables, health checks, and networking for the following application:"
  },
  {
    "id": 12,
    "category": "coding",
    "title": "CI/CD Pipeline",
    "prompt": "Design a complete CI/CD pipeline with automated testing, code quality checks, security scanning, staging deployment, and production release strategy for:"
  },
  {
    "id": 13,
    "category": "coding",
    "title": "GraphQL API",
    "prompt": "Build a complete GraphQL API with queries, mutations, subscriptions, authentication, pagination, and error handling for the following use case:"
  },
  {
    "id": 14,
    "category": "coding",
    "title": "Microservices Design",
    "prompt": "Design a microservices architecture with service boundaries, inter-service communication, event sourcing, and fault tolerance for the following system:"
  },
  {
    "id": 15,
    "category": "coding",
    "title": "WebSocket Implementation",
    "prompt": "Implement a real-time WebSocket system with connection management, room support, authentication, reconnection logic, and scaling strategy for:"
  },
  {
    "id": 16,
    "category": "coding",
    "title": "Machine Learning Model",
    "prompt": "Build a complete machine learning pipeline including data preprocessing, feature engineering, model selection, training, evaluation, and deployment for:"
  },
  {
    "id": 17,
    "category": "coding",
    "title": "Browser Extension",
    "prompt": "Build a complete Chrome extension with manifest v3, background service worker, content scripts, popup UI, and storage management for:"
  },
  {
    "id": 18,
    "category": "coding",
    "title": "CLI Tool",
    "prompt": "Build a professional command-line tool with argument parsing, interactive prompts, colored output, error handling, and help documentation for:"
  },
  {
    "id": 19,
    "category": "coding",
    "title": "Web Scraper",
    "prompt": "Build a robust web scraper with rate limiting, proxy rotation, CAPTCHA handling, data extraction, and structured storage for the following website:"
  },
  {
    "id": 20,
    "category": "coding",
    "title": "Authentication System",
    "prompt": "Implement a complete authentication system with JWT, OAuth2, refresh tokens, role-based access control, session management, and security headers for:"
  },
  {
    "id": 21,
    "category": "coding",
    "title": "Payment Integration",
    "prompt": "Integrate a complete payment system with Stripe including subscriptions, webhooks, refunds, invoice generation, and PCI compliance for:"
  },
  {
    "id": 22,
    "category": "coding",
    "title": "Real-time Dashboard",
    "prompt": "Build a real-time analytics dashboard with live data updates, WebSocket connections, chart visualizations, and filtering capabilities for:"
  },
  {
    "id": 23,
    "category": "coding",
    "title": "File Upload System",
    "prompt": "Build a secure file upload system with chunked uploads, progress tracking, virus scanning, CDN integration, and access control for:"
  },
  {
    "id": 24,
    "category": "coding",
    "title": "Search Engine",
    "prompt": "Implement a full-text search engine with fuzzy matching, filters, facets, ranking, autocomplete, and analytics for the following dataset:"
  },
  {
    "id": 25,
    "category": "coding",
    "title": "Caching Strategy",
    "prompt": "Design and implement a comprehensive caching strategy with Redis, cache invalidation, TTL management, and cache warming for the following application:"
  },
  {
    "id": 26,
    "category": "coding",
    "title": "Email System",
    "prompt": "Build a complete email system with templates, queuing, retry logic, bounce handling, analytics tracking, and spam compliance for:"
  },
  {
    "id": 27,
    "category": "coding",
    "title": "Notification System",
    "prompt": "Build a multi-channel notification system supporting push, email, SMS, and in-app notifications with user preferences and delivery tracking for:"
  },
  {
    "id": 28,
    "category": "coding",
    "title": "API Rate Limiter",
    "prompt": "Implement a sophisticated API rate limiting system with multiple tiers, sliding windows, burst allowances, and Redis-backed tracking for:"
  },
  {
    "id": 29,
    "category": "coding",
    "title": "Data Pipeline",
    "prompt": "Design a complete ETL data pipeline with data validation, transformation, error handling, logging, and monitoring for:"
  },
  {
    "id": 30,
    "category": "coding",
    "title": "Serverless Functions",
    "prompt": "Design and implement a serverless architecture with AWS Lambda or Vercel Functions, including triggers, environment management, and cold start optimization for:"
  },
  {
    "id": 31,
    "category": "coding",
    "title": "Mobile App Backend",
    "prompt": "Design a complete mobile app backend with offline sync, push notifications, user management, analytics, and crash reporting for:"
  },
  {
    "id": 32,
    "category": "coding",
    "title": "Blockchain Smart Contract",
    "prompt": "Write a secure Solidity smart contract with proper access control, events, error handling, and gas optimization for the following use case:"
  },
  {
    "id": 33,
    "category": "coding",
    "title": "Browser Automation",
    "prompt": "Write a Playwright or Puppeteer script for complete browser automation with login handling, data extraction, screenshot capture, and error recovery for:"
  },
  {
    "id": 34,
    "category": "coding",
    "title": "Code Documentation",
    "prompt": "Generate comprehensive technical documentation including API reference, setup guide, architecture overview, and code examples for the following codebase:"
  },
  {
    "id": 35,
    "category": "coding",
    "title": "Regex Patterns",
    "prompt": "Write precise, optimized regular expressions with full explanation, edge case handling, and test cases for the following validation requirements:"
  },
  {
    "id": 36,
    "category": "coding",
    "title": "Data Structures",
    "prompt": "Implement the following custom data structure with all operations, time complexity analysis, and practical usage examples:"
  },
  {
    "id": 37,
    "category": "coding",
    "title": "Design Patterns",
    "prompt": "Implement the following design pattern with a real-world example, UML diagram description, pros/cons analysis, and when to use it:"
  },
  {
    "id": 38,
    "category": "coding",
    "title": "Error Handling",
    "prompt": "Design a comprehensive error handling strategy with custom error classes, logging, user-friendly messages, and recovery mechanisms for:"
  },
  {
    "id": 39,
    "category": "coding",
    "title": "State Management",
    "prompt": "Implement a complete state management solution with actions, reducers, selectors, middleware, and dev tools integration for the following application:"
  },
  {
    "id": 40,
    "category": "coding",
    "title": "Code Generator",
    "prompt": "Build a code generation tool that creates boilerplate code, follows project conventions, and generates tests automatically for:"
  },
  {
    "id": 41,
    "category": "coding",
    "title": "Load Testing",
    "prompt": "Write a comprehensive load testing script with ramp-up scenarios, stress tests, spike tests, and performance benchmarks for:"
  },
  {
    "id": 42,
    "category": "coding",
    "title": "Memory Optimization",
    "prompt": "Analyze and optimize memory usage in the following code. Identify leaks, unnecessary allocations, and implement efficient memory management:"
  },
  {
    "id": 43,
    "category": "coding",
    "title": "Async Programming",
    "prompt": "Refactor the following synchronous code to fully async/await with proper error handling, concurrency control, and cancellation support:"
  },
  {
    "id": 44,
    "category": "coding",
    "title": "Type System",
    "prompt": "Add comprehensive TypeScript types, generics, conditional types, and runtime validation to the following JavaScript codebase:"
  },
  {
    "id": 45,
    "category": "coding",
    "title": "Plugin Architecture",
    "prompt": "Design an extensible plugin architecture with lifecycle hooks, dependency injection, sandboxing, and version compatibility for:"
  },
  {
    "id": 46,
    "category": "coding",
    "title": "Event System",
    "prompt": "Implement a robust event-driven system with pub/sub, event sourcing, replay capability, and dead letter queue for:"
  },
  {
    "id": 47,
    "category": "coding",
    "title": "Configuration Management",
    "prompt": "Build a hierarchical configuration management system with environment overrides, validation, secrets management, and hot reload for:"
  },
  {
    "id": 48,
    "category": "coding",
    "title": "Logging System",
    "prompt": "Implement a structured logging system with log levels, correlation IDs, log aggregation, alerting, and log rotation for:"
  },
  {
    "id": 49,
    "category": "coding",
    "title": "Testing Strategy",
    "prompt": "Design a complete testing strategy with unit, integration, e2e, performance, and security tests including CI integration for:"
  },
  {
    "id": 50,
    "category": "coding",
    "title": "Code Splitting",
    "prompt": "Implement optimal code splitting with dynamic imports, lazy loading, prefetching strategy, and bundle analysis for:"
  },
  {
    "id": 51,
    "category": "writing",
    "title": "SEO Blog Post",
    "prompt": "Write a deeply researched, SEO-optimized long-form blog post (2000+ words) with compelling title, meta description, headers, internal linking suggestions, FAQs, and strong CTA about:"
  },
  {
    "id": 52,
    "category": "writing",
    "title": "Professional Email",
    "prompt": "Write a highly professional, persuasive email that clearly communicates the message, respects the recipient's time, uses proper tone, and drives the desired action for:"
  },
  {
    "id": 53,
    "category": "writing",
    "title": "Short Story",
    "prompt": "Write a gripping short story with a compelling hook, well-developed characters, vivid sensory descriptions, building tension, and a satisfying or unexpected ending about:"
  },
  {
    "id": 54,
    "category": "writing",
    "title": "Product Description",
    "prompt": "Write a conversion-optimized product description that paints a vivid picture, addresses objections, highlights benefits over features, and creates urgency for:"
  },
  {
    "id": 55,
    "category": "writing",
    "title": "Cover Letter",
    "prompt": "Write a standout cover letter that tells a compelling career story, highlights quantifiable achievements, shows company research, and expresses genuine enthusiasm for:"
  },
  {
    "id": 56,
    "category": "writing",
    "title": "White Paper",
    "prompt": "Write a comprehensive industry white paper with executive summary, research findings, data analysis, expert insights, and actionable recommendations about:"
  },
  {
    "id": 57,
    "category": "writing",
    "title": "Press Release",
    "prompt": "Write a professional press release following AP style with compelling headline, strong lead paragraph, supporting quotes, and clear news hook for:"
  },
  {
    "id": 58,
    "category": "writing",
    "title": "Technical Documentation",
    "prompt": "Write clear, comprehensive technical documentation with getting started guide, API reference, code examples, troubleshooting, and FAQs for:"
  },
  {
    "id": 59,
    "category": "writing",
    "title": "Speech Writing",
    "prompt": "Write a powerful, memorable speech with strong opening hook, clear narrative arc, emotional resonance, rhetorical devices, and inspiring conclusion for:"
  },
  {
    "id": 60,
    "category": "writing",
    "title": "Grant Proposal",
    "prompt": "Write a compelling grant proposal with clear problem statement, proposed solution, measurable outcomes, timeline, budget justification, and organizational credibility for:"
  },
  {
    "id": 61,
    "category": "writing",
    "title": "Newsletter",
    "prompt": "Write an engaging email newsletter with attention-grabbing subject line, valuable content sections, personal tone, and clear CTAs for:"
  },
  {
    "id": 62,
    "category": "writing",
    "title": "Case Study",
    "prompt": "Write a detailed case study with client background, challenge, solution, implementation process, measurable results, and testimonial for:"
  },
  {
    "id": 63,
    "category": "writing",
    "title": "Executive Summary",
    "prompt": "Write a concise, impactful executive summary that captures key findings, strategic recommendations, and decision points for:"
  },
  {
    "id": 64,
    "category": "writing",
    "title": "Research Paper",
    "prompt": "Write a well-structured academic research paper with abstract, literature review, methodology, findings, discussion, and conclusion about:"
  },
  {
    "id": 65,
    "category": "writing",
    "title": "Sales Script",
    "prompt": "Write a high-converting sales script with rapport building, discovery questions, value proposition, objection handling, and closing techniques for:"
  },
  {
    "id": 66,
    "category": "writing",
    "title": "Podcast Script",
    "prompt": "Write an engaging podcast episode script with compelling intro, interview questions, smooth transitions, key talking points, and memorable outro for:"
  },
  {
    "id": 67,
    "category": "writing",
    "title": "Video Script",
    "prompt": "Write a compelling YouTube video script with strong hook, clear structure, engaging narration, B-roll suggestions, and strong CTA for:"
  },
  {
    "id": 68,
    "category": "writing",
    "title": "Landing Page Copy",
    "prompt": "Write high-converting landing page copy with powerful headline, subheadline, benefit bullets, social proof, FAQ section, and multiple CTAs for:"
  },
  {
    "id": 69,
    "category": "writing",
    "title": "About Us Page",
    "prompt": "Write a compelling About Us page that tells the brand story, communicates values, builds trust, shows personality, and connects emotionally with visitors for:"
  },
  {
    "id": 70,
    "category": "writing",
    "title": "Mission Statement",
    "prompt": "Write a powerful, authentic mission statement that captures the organization's purpose, values, and impact for:"
  },
  {
    "id": 71,
    "category": "writing",
    "title": "Annual Report",
    "prompt": "Write an engaging annual report narrative with highlights, achievements, challenges overcome, financial narrative, and future outlook for:"
  },
  {
    "id": 72,
    "category": "writing",
    "title": "User Manual",
    "prompt": "Write a clear, user-friendly manual with step-by-step instructions, troubleshooting guide, safety warnings, and helpful tips for:"
  },
  {
    "id": 73,
    "category": "writing",
    "title": "Proposal Document",
    "prompt": "Write a winning business proposal with executive summary, problem analysis, proposed solution, timeline, pricing, and terms for:"
  },
  {
    "id": 74,
    "category": "writing",
    "title": "Opinion Essay",
    "prompt": "Write a well-argued opinion essay with clear thesis, supporting evidence, counterargument acknowledgment, and persuasive conclusion about:"
  },
  {
    "id": 75,
    "category": "writing",
    "title": "LinkedIn Article",
    "prompt": "Write a thought-leadership LinkedIn article with provocative title, personal story, industry insights, actionable advice, and engagement questions about:"
  },
  {
    "id": 76,
    "category": "writing",
    "title": "Book Summary",
    "prompt": "Write a comprehensive book summary with key concepts, main arguments, practical takeaways, critical analysis, and reading recommendation for:"
  },
  {
    "id": 77,
    "category": "writing",
    "title": "FAQ Document",
    "prompt": "Write a comprehensive FAQ document that anticipates all customer questions, provides clear answers, and reduces support burden for:"
  },
  {
    "id": 78,
    "category": "writing",
    "title": "Job Description",
    "prompt": "Write a compelling job description that attracts top talent, clearly defines responsibilities, communicates culture, and stands out from competitors for:"
  },
  {
    "id": 79,
    "category": "writing",
    "title": "Terms of Service",
    "prompt": "Write clear, fair Terms of Service that protect the business, respect users, are written in plain language, and cover all key legal areas for:"
  },
  {
    "id": 80,
    "category": "writing",
    "title": "Investor Update",
    "prompt": "Write a compelling monthly investor update with key metrics, progress highlights, challenges, upcoming milestones, and ask for:"
  },
  {
    "id": 81,
    "category": "writing",
    "title": "Thought Leadership Piece",
    "prompt": "Write a provocative thought leadership article that challenges industry assumptions, presents fresh perspective, and establishes authority about:"
  },
  {
    "id": 82,
    "category": "writing",
    "title": "Ebook Chapter",
    "prompt": "Write an engaging ebook chapter with clear learning objectives, actionable content, real-world examples, exercises, and key takeaways about:"
  },
  {
    "id": 83,
    "category": "writing",
    "title": "Testimonial Request",
    "prompt": "Write a testimonial request email that makes it easy for clients, provides guiding questions, explains how it will be used, and shows appreciation for:"
  },
  {
    "id": 84,
    "category": "writing",
    "title": "Apology Letter",
    "prompt": "Write a sincere, professional apology letter that takes full responsibility, explains what happened, outlines corrective actions, and rebuilds trust for:"
  },
  {
    "id": 85,
    "category": "writing",
    "title": "Welcome Email Series",
    "prompt": "Write a 5-email welcome sequence that onboards new users, delivers value progressively, builds relationship, and drives key actions for:"
  },
  {
    "id": 86,
    "category": "writing",
    "title": "Biography",
    "prompt": "Write a compelling professional biography in first and third person that highlights achievements, personality, expertise, and unique journey for:"
  },
  {
    "id": 87,
    "category": "writing",
    "title": "Manifesto",
    "prompt": "Write a powerful brand or personal manifesto that declares core beliefs, challenges the status quo, inspires action, and creates a movement for:"
  },
  {
    "id": 88,
    "category": "writing",
    "title": "Training Material",
    "prompt": "Write comprehensive training materials with learning objectives, content modules, activities, assessments, and facilitator guide for:"
  },
  {
    "id": 89,
    "category": "writing",
    "title": "Policy Document",
    "prompt": "Write a clear, enforceable company policy document that covers all scenarios, uses plain language, and is easy to follow for:"
  },
  {
    "id": 90,
    "category": "writing",
    "title": "Comparison Article",
    "prompt": "Write a thorough, unbiased comparison article with evaluation criteria, detailed analysis, pros/cons tables, and clear recommendation for:"
  },
  {
    "id": 91,
    "category": "writing",
    "title": "How-To Guide",
    "prompt": "Write a detailed, beginner-friendly how-to guide with prerequisites, step-by-step instructions, screenshots descriptions, tips, and troubleshooting for:"
  },
  {
    "id": 92,
    "category": "writing",
    "title": "Interview Questions",
    "prompt": "Write 30 powerful interview questions with follow-up probes, what to look for in answers, and red flags for the following role:"
  },
  {
    "id": 93,
    "category": "writing",
    "title": "Feedback Report",
    "prompt": "Write a constructive, detailed feedback report with specific observations, impact analysis, improvement suggestions, and encouragement for:"
  },
  {
    "id": 94,
    "category": "writing",
    "title": "Company Newsletter",
    "prompt": "Write an engaging internal company newsletter with culture highlights, team news, project updates, recognition section, and upcoming events for:"
  },
  {
    "id": 95,
    "category": "writing",
    "title": "Product Launch Email",
    "prompt": "Write a high-anticipation product launch email sequence (3 emails) with teaser, launch day, and follow-up for:"
  },
  {
    "id": 96,
    "category": "writing",
    "title": "Webinar Description",
    "prompt": "Write a compelling webinar description with clear value proposition, what attendees will learn, speaker credibility, and urgency to register for:"
  },
  {
    "id": 97,
    "category": "writing",
    "title": "Social Proof Page",
    "prompt": "Write a compelling social proof and testimonials page that builds maximum trust and credibility for:"
  },
  {
    "id": 98,
    "category": "writing",
    "title": "Resignation Letter",
    "prompt": "Write a professional, gracious resignation letter that maintains relationships, expresses gratitude, and transitions smoothly for:"
  },
  {
    "id": 99,
    "category": "writing",
    "title": "Recommendation Letter",
    "prompt": "Write a powerful recommendation letter with specific examples, measurable achievements, character assessment, and strong endorsement for:"
  },
  {
    "id": 100,
    "category": "business",
    "title": "Business Plan",
    "prompt": "Create a comprehensive 10-section business plan with executive summary, market analysis, competitive landscape, product/service description, marketing strategy, operations plan, team bios, financial projections, funding requirements, and exit strategy for:"
  },
  {
    "id": 101,
    "category": "business",
    "title": "SWOT Analysis",
    "prompt": "Conduct an expert-level SWOT analysis with detailed internal strengths and weaknesses, external opportunities and threats, strategic implications, and prioritized action items for:"
  },
  {
    "id": 102,
    "category": "business",
    "title": "Go-To-Market Strategy",
    "prompt": "Develop a complete go-to-market strategy with market segmentation, ideal customer profile, positioning, pricing strategy, distribution channels, launch timeline, and success metrics for:"
  },
  {
    "id": 103,
    "category": "business",
    "title": "Financial Model",
    "prompt": "Build a detailed 3-year financial model with revenue projections, cost structure, unit economics, cash flow analysis, break-even analysis, and scenario planning for:"
  },
  {
    "id": 104,
    "category": "business",
    "title": "Competitive Analysis",
    "prompt": "Conduct a deep competitive analysis with market positioning matrix, feature comparison, pricing analysis, SWOT for each competitor, and strategic recommendations for:"
  },
  {
    "id": 105,
    "category": "business",
    "title": "Investor Pitch Deck",
    "prompt": "Create a compelling 12-slide investor pitch deck outline with problem, solution, market size, traction, business model, team, financials, and ask for:"
  },
  {
    "id": 106,
    "category": "business",
    "title": "OKR Framework",
    "prompt": "Design a complete OKR (Objectives and Key Results) framework with company, department, and individual OKRs, tracking system, and review cadence for:"
  },
  {
    "id": 107,
    "category": "business",
    "title": "Customer Journey Map",
    "prompt": "Create a detailed customer journey map with all touchpoints, emotions, pain points, opportunities, and improvement recommendations for:"
  },
  {
    "id": 108,
    "category": "business",
    "title": "Pricing Strategy",
    "prompt": "Develop a comprehensive pricing strategy with market research, value-based pricing analysis, tier structure, competitive positioning, and testing plan for:"
  },
  {
    "id": 109,
    "category": "business",
    "title": "Partnership Proposal",
    "prompt": "Write a compelling strategic partnership proposal with mutual value proposition, partnership structure, revenue sharing model, and implementation plan for:"
  },
  {
    "id": 110,
    "category": "business",
    "title": "Risk Management Plan",
    "prompt": "Create a comprehensive risk management plan with risk identification, probability-impact matrix, mitigation strategies, contingency plans, and monitoring system for:"
  },
  {
    "id": 111,
    "category": "business",
    "title": "Operations Manual",
    "prompt": "Create a detailed operations manual with standard operating procedures, quality standards, performance metrics, training requirements, and continuous improvement process for:"
  },
  {
    "id": 112,
    "category": "business",
    "title": "Brand Strategy",
    "prompt": "Develop a complete brand strategy with brand identity, positioning statement, voice and tone, visual guidelines, messaging framework, and brand governance for:"
  },
  {
    "id": 113,
    "category": "business",
    "title": "Customer Retention Strategy",
    "prompt": "Design a comprehensive customer retention strategy with loyalty program, churn prediction, win-back campaigns, NPS improvement, and lifetime value optimization for:"
  },
  {
    "id": 114,
    "category": "business",
    "title": "Sales Playbook",
    "prompt": "Create a complete sales playbook with ideal customer profile, sales process, discovery questions, objection handling, proposal templates, and closing techniques for:"
  },
  {
    "id": 115,
    "category": "business",
    "title": "Board Presentation",
    "prompt": "Create a comprehensive board presentation with business performance dashboard, strategic updates, key decisions needed, risks, and 90-day roadmap for:"
  },
  {
    "id": 116,
    "category": "business",
    "title": "Due Diligence Checklist",
    "prompt": "Create a comprehensive due diligence checklist covering financials, legal, operations, technology, team, market, and customers for:"
  },
  {
    "id": 117,
    "category": "business",
    "title": "Product Roadmap",
    "prompt": "Design a strategic product roadmap with vision, themes, initiatives, features, release timeline, dependencies, and success metrics for:"
  },
  {
    "id": 118,
    "category": "business",
    "title": "Hiring Strategy",
    "prompt": "Develop a complete hiring strategy with workforce planning, job architecture, sourcing channels, interview process, employer branding, and onboarding program for:"
  },
  {
    "id": 119,
    "category": "business",
    "title": "Crisis Management Plan",
    "prompt": "Create a comprehensive crisis management plan with scenario playbooks, communication templates, escalation procedures, and post-crisis review process for:"
  },
  {
    "id": 120,
    "category": "business",
    "title": "Franchise Business Model",
    "prompt": "Design a complete franchise business model with franchise fee structure, training program, support system, quality control, and franchisee selection criteria for:"
  },
  {
    "id": 121,
    "category": "business",
    "title": "Subscription Business Model",
    "prompt": "Design an optimized subscription business model with tier structure, pricing, free trial strategy, upgrade triggers, and churn reduction mechanisms for:"
  },
  {
    "id": 122,
    "category": "business",
    "title": "Market Entry Strategy",
    "prompt": "Develop a complete market entry strategy with market assessment, entry mode selection, localization requirements, regulatory compliance, and phased rollout plan for:"
  },
  {
    "id": 123,
    "category": "business",
    "title": "Customer Success Program",
    "prompt": "Design a comprehensive customer success program with onboarding journey, health scoring, QBR process, expansion playbook, and advocacy program for:"
  },
  {
    "id": 124,
    "category": "business",
    "title": "Supply Chain Optimization",
    "prompt": "Analyze and optimize the supply chain with vendor evaluation, inventory management, logistics optimization, risk mitigation, and cost reduction strategy for:"
  },
  {
    "id": 125,
    "category": "business",
    "title": "Digital Transformation Roadmap",
    "prompt": "Create a comprehensive digital transformation roadmap with current state assessment, technology stack, change management, quick wins, and long-term vision for:"
  },
  {
    "id": 126,
    "category": "business",
    "title": "Revenue Operations Strategy",
    "prompt": "Design a complete RevOps strategy aligning sales, marketing, and customer success with shared metrics, processes, technology, and reporting for:"
  },
  {
    "id": 127,
    "category": "business",
    "title": "Expansion Strategy",
    "prompt": "Develop a detailed market expansion strategy with target market selection, localization plan, resource requirements, risk assessment, and success milestones for:"
  },
  {
    "id": 128,
    "category": "business",
    "title": "Exit Strategy",
    "prompt": "Develop a comprehensive exit strategy with valuation methodology, potential acquirers, M&A preparation checklist, negotiation strategy, and timeline for:"
  },
  {
    "id": 129,
    "category": "business",
    "title": "Performance Review System",
    "prompt": "Design a fair, effective performance review system with competency framework, rating scales, calibration process, development planning, and compensation linkage for:"
  },
  {
    "id": 130,
    "category": "business",
    "title": "Innovation Framework",
    "prompt": "Create a structured innovation framework with ideation process, validation methodology, resource allocation, portfolio management, and culture building for:"
  },
  {
    "id": 131,
    "category": "business",
    "title": "Customer Segmentation",
    "prompt": "Perform detailed customer segmentation analysis with demographic, psychographic, behavioral, and needs-based segments, personas, and tailored strategies for:"
  },
  {
    "id": 132,
    "category": "business",
    "title": "Procurement Strategy",
    "prompt": "Develop a comprehensive procurement strategy with vendor selection criteria, RFP process, contract management, supplier relationship, and cost optimization for:"
  },
  {
    "id": 133,
    "category": "business",
    "title": "KPI Dashboard",
    "prompt": "Design a comprehensive KPI dashboard with leading and lagging indicators, targets, visualization recommendations, and review cadence for:"
  },
  {
    "id": 134,
    "category": "business",
    "title": "Merger Integration Plan",
    "prompt": "Create a detailed merger integration plan with workstreams, cultural alignment, systems consolidation, communication plan, and synergy realization for:"
  },
  {
    "id": 135,
    "category": "business",
    "title": "B2B Sales Strategy",
    "prompt": "Develop a complete B2B sales strategy with account targeting, multi-threading approach, champion building, procurement navigation, and enterprise closing process for:"
  },
  {
    "id": 136,
    "category": "business",
    "title": "Loyalty Program Design",
    "prompt": "Design a compelling loyalty program with points structure, tier benefits, earning mechanics, redemption options, and gamification elements for:"
  },
  {
    "id": 137,
    "category": "business",
    "title": "Outsourcing Strategy",
    "prompt": "Develop a comprehensive outsourcing strategy with build/buy/partner analysis, vendor evaluation, SLA framework, governance model, and transition plan for:"
  },
  {
    "id": 138,
    "category": "business",
    "title": "Content Marketing Strategy",
    "prompt": "Create a complete content marketing strategy with audience personas, content pillars, editorial calendar, distribution channels, promotion plan, and ROI measurement for:"
  },
  {
    "id": 139,
    "category": "business",
    "title": "Customer Feedback System",
    "prompt": "Design a comprehensive customer feedback system with survey design, NPS program, feedback loops, analysis process, and action planning for:"
  },
  {
    "id": 140,
    "category": "business",
    "title": "Change Management Plan",
    "prompt": "Create a detailed change management plan with stakeholder analysis, communication strategy, training plan, resistance management, and adoption measurement for:"
  },
  {
    "id": 141,
    "category": "business",
    "title": "Strategic Planning Process",
    "prompt": "Design a complete annual strategic planning process with environmental scan, strategy formulation, goal setting, resource allocation, and execution monitoring for:"
  },
  {
    "id": 142,
    "category": "business",
    "title": "Vendor Management Program",
    "prompt": "Create a comprehensive vendor management program with onboarding process, performance scorecards, relationship tiers, review cadence, and risk monitoring for:"
  },
  {
    "id": 143,
    "category": "business",
    "title": "Employee Engagement Strategy",
    "prompt": "Develop a holistic employee engagement strategy with pulse surveys, recognition programs, career development, manager effectiveness, and culture initiatives for:"
  },
  {
    "id": 144,
    "category": "business",
    "title": "Business Continuity Plan",
    "prompt": "Create a comprehensive business continuity plan with recovery objectives, backup systems, communication protocols, team roles, and testing schedule for:"
  },
  {
    "id": 145,
    "category": "business",
    "title": "Affiliate Program Design",
    "prompt": "Design a high-performing affiliate program with commission structure, partner tiers, promotional materials, tracking system, and recruitment strategy for:"
  },
  {
    "id": 146,
    "category": "business",
    "title": "Unit Economics Analysis",
    "prompt": "Perform a detailed unit economics analysis with CAC, LTV, payback period, contribution margin, and optimization recommendations for:"
  },
  {
    "id": 147,
    "category": "business",
    "title": "Fundraising Strategy",
    "prompt": "Develop a comprehensive fundraising strategy with investor targeting, pitch narrative, data room preparation, term sheet guidance, and closing process for:"
  },
  {
    "id": 148,
    "category": "business",
    "title": "Community Building Strategy",
    "prompt": "Design a comprehensive community strategy with platform selection, content programming, engagement mechanics, moderation guidelines, and growth plan for:"
  },
  {
    "id": 149,
    "category": "education",
    "title": "Explain Like I'm 5",
    "prompt": "Explain the following complex concept using simple language, relatable everyday analogies, fun examples a child would understand, and a memorable summary. Make it stick:"
  },
  {
    "id": 150,
    "category": "education",
    "title": "Comprehensive Study Guide",
    "prompt": "Create an expert-level study guide with concept explanations, key definitions, visual diagram descriptions, memory techniques, practice questions with answers, and exam tips for:"
  },
  {
    "id": 151,
    "category": "education",
    "title": "Detailed Lesson Plan",
    "prompt": "Design a complete lesson plan with learning objectives, prerequisite knowledge, warm-up activity, main instruction, guided practice, independent practice, assessment, and differentiation strategies for:"
  },
  {
    "id": 152,
    "category": "education",
    "title": "Quiz Generator",
    "prompt": "Generate 30 varied assessment questions (multiple choice, true/false, short answer, and essay) with answer key, difficulty ratings, and learning objective alignment for:"
  },
  {
    "id": 153,
    "category": "education",
    "title": "Research Paper Outline",
    "prompt": "Create a detailed research paper outline with thesis statement, literature review structure, methodology section, argument flow, evidence requirements, and citation strategy for:"
  },
  {
    "id": 154,
    "category": "education",
    "title": "Curriculum Design",
    "prompt": "Design a complete curriculum with unit structure, learning progressions, standards alignment, assessment plan, resources list, and pacing guide for:"
  },
  {
    "id": 155,
    "category": "education",
    "title": "Socratic Discussion Guide",
    "prompt": "Create a Socratic seminar guide with essential questions, text-based evidence prompts, discussion protocols, facilitation strategies, and reflection activities for:"
  },
  {
    "id": 156,
    "category": "education",
    "title": "Differentiated Instruction",
    "prompt": "Design differentiated instruction strategies for visual, auditory, kinesthetic, and reading/writing learners with specific activities, modifications, and enrichment options for:"
  },
  {
    "id": 157,
    "category": "education",
    "title": "Project-Based Learning",
    "prompt": "Design a complete project-based learning unit with driving question, project brief, milestones, rubrics, collaboration guidelines, and presentation format for:"
  },
  {
    "id": 158,
    "category": "education",
    "title": "Flipped Classroom",
    "prompt": "Design a flipped classroom experience with pre-class video content outline, in-class activity design, accountability check, and assessment strategy for:"
  },
  {
    "id": 159,
    "category": "education",
    "title": "Formative Assessment",
    "prompt": "Create 10 creative formative assessment strategies with implementation guide, data collection methods, and responsive teaching suggestions for:"
  },
  {
    "id": 160,
    "category": "education",
    "title": "Learning Objectives",
    "prompt": "Write precise learning objectives using Bloom's Taxonomy at all six levels (remember, understand, apply, analyze, evaluate, create) with assessment suggestions for:"
  },
  {
    "id": 161,
    "category": "education",
    "title": "Concept Map",
    "prompt": "Create a detailed concept map with main concept, subconcepts, relationships, examples, and cross-connections for the following topic:"
  },
  {
    "id": 162,
    "category": "education",
    "title": "Debate Framework",
    "prompt": "Design a complete debate framework with resolution, position arguments, evidence requirements, counterargument strategies, rebuttal guides, and judging criteria for:"
  },
  {
    "id": 163,
    "category": "education",
    "title": "Reading Comprehension",
    "prompt": "Create a comprehensive reading comprehension activity with pre-reading strategies, during-reading questions, post-reading analysis, vocabulary work, and extension activities for:"
  },
  {
    "id": 164,
    "category": "education",
    "title": "Science Experiment",
    "prompt": "Design a complete science experiment with hypothesis formation, materials list, step-by-step procedure, data collection table, analysis questions, and conclusion framework for:"
  },
  {
    "id": 165,
    "category": "education",
    "title": "Math Problem Set",
    "prompt": "Create a progressive math problem set starting from basic recall to complex application with worked examples, hints, common mistakes to avoid, and extension problems for:"
  },
  {
    "id": 166,
    "category": "education",
    "title": "Historical Analysis",
    "prompt": "Design a historical thinking activity with primary source analysis, contextualization, corroboration, close reading, and evidence-based argument construction for:"
  },
  {
    "id": 167,
    "category": "education",
    "title": "Language Learning",
    "prompt": "Create a comprehensive language learning plan with vocabulary acquisition, grammar instruction, speaking practice, listening activities, and cultural immersion strategies for:"
  },
  {
    "id": 168,
    "category": "education",
    "title": "Critical Thinking Skills",
    "prompt": "Design lessons specifically targeting critical thinking with logical reasoning, bias identification, argument evaluation, evidence assessment, and perspective-taking for:"
  },
  {
    "id": 169,
    "category": "education",
    "title": "STEM Challenge",
    "prompt": "Design a complete STEM challenge with real-world problem scenario, design constraints, building phase, testing protocol, reflection questions, and presentation format for:"
  },
  {
    "id": 170,
    "category": "education",
    "title": "Peer Learning Activity",
    "prompt": "Design a structured peer learning activity with roles, protocols, quality control, accountability measures, and reflection process for:"
  },
  {
    "id": 171,
    "category": "education",
    "title": "Portfolio Assessment",
    "prompt": "Design a comprehensive portfolio assessment system with artifact selection guidelines, reflection prompts, evaluation rubric, and conference protocol for:"
  },
  {
    "id": 172,
    "category": "education",
    "title": "Online Course Design",
    "prompt": "Design a complete online course with module structure, video script outlines, interactive activities, discussion prompts, quizzes, and completion certificates for:"
  },
  {
    "id": 173,
    "category": "education",
    "title": "Study Skills Workshop",
    "prompt": "Design a study skills workshop with time management, note-taking methods, memory techniques, test-taking strategies, and stress management for students:"
  },
  {
    "id": 174,
    "category": "education",
    "title": "Gifted Education Program",
    "prompt": "Design an enrichment program for gifted learners with acceleration options, independent study, mentorship, competition preparation, and advanced projects for:"
  },
  {
    "id": 175,
    "category": "education",
    "title": "Special Education Accommodation",
    "prompt": "Create comprehensive IEP-aligned accommodations and modifications with specific strategies, assistive technology, environmental supports, and progress monitoring for:"
  },
  {
    "id": 176,
    "category": "education",
    "title": "Teacher Professional Development",
    "prompt": "Design a professional development workshop with adult learning principles, collaborative activities, practice time, coaching protocol, and follow-up support for:"
  },
  {
    "id": 177,
    "category": "education",
    "title": "Parent Engagement Strategy",
    "prompt": "Design a family engagement program with communication plan, home learning activities, volunteer opportunities, and two-way feedback system for:"
  },
  {
    "id": 178,
    "category": "education",
    "title": "Educational Game Design",
    "prompt": "Design an educational game with learning objectives, game mechanics, progression system, assessment integration, and engagement strategies for:"
  },
  {
    "id": 179,
    "category": "education",
    "title": "Inquiry-Based Learning",
    "prompt": "Design an inquiry-based learning experience with compelling question, investigation process, evidence gathering, sense-making, and presentation for:"
  },
  {
    "id": 180,
    "category": "education",
    "title": "Cross-Curricular Integration",
    "prompt": "Design a cross-curricular unit connecting multiple subjects with shared themes, collaborative activities, and integrated assessments for:"
  },
  {
    "id": 181,
    "category": "education",
    "title": "Cultural Responsiveness",
    "prompt": "Design culturally responsive lessons that honor diverse backgrounds, include multiple perspectives, use relevant contexts, and build on community knowledge for:"
  },
  {
    "id": 182,
    "category": "education",
    "title": "Classroom Management",
    "prompt": "Design a comprehensive classroom management system with expectations, routines, positive behavior support, intervention ladder, and restorative practices for:"
  },
  {
    "id": 183,
    "category": "education",
    "title": "Student-Led Conferences",
    "prompt": "Design a student-led conference protocol with preparation activities, portfolio selection, talking points, goal setting, and family guidance for:"
  },
  {
    "id": 184,
    "category": "education",
    "title": "Mastery Learning",
    "prompt": "Design a mastery learning system with competency map, formative checkpoints, reteaching strategies, enrichment options, and progress tracking for:"
  },
  {
    "id": 185,
    "category": "education",
    "title": "Visible Thinking",
    "prompt": "Design visible thinking routines with thinking prompts, documentation strategies, making thinking public, and connecting to content standards for:"
  },
  {
    "id": 186,
    "category": "education",
    "title": "Growth Mindset Program",
    "prompt": "Design a growth mindset program with mindset assessments, lesson activities, language shifts, feedback protocols, and culture building strategies for:"
  },
  {
    "id": 187,
    "category": "education",
    "title": "Digital Literacy Curriculum",
    "prompt": "Design a digital literacy curriculum covering information evaluation, online safety, digital citizenship, media creation, and ethical use for:"
  },
  {
    "id": 188,
    "category": "education",
    "title": "Financial Literacy Lessons",
    "prompt": "Design age-appropriate financial literacy lessons covering budgeting, saving, investing, credit, insurance, and entrepreneurship for:"
  },
  {
    "id": 189,
    "category": "education",
    "title": "Environmental Education",
    "prompt": "Design an environmental education unit with ecological concepts, local issues, action project, citizen science component, and advocacy skills for:"
  },
  {
    "id": 190,
    "category": "education",
    "title": "Social Emotional Learning",
    "prompt": "Design a comprehensive SEL program covering self-awareness, self-management, social awareness, relationship skills, and responsible decision-making for:"
  },
  {
    "id": 191,
    "category": "education",
    "title": "Career Exploration",
    "prompt": "Design a career exploration program with interest assessments, industry research, informational interviews, job shadowing, and pathway planning for:"
  },
  {
    "id": 192,
    "category": "education",
    "title": "Maker Education",
    "prompt": "Design a maker education experience with design thinking process, tools introduction, open-ended project, iteration cycles, and showcase event for:"
  },
  {
    "id": 193,
    "category": "education",
    "title": "Philosophy for Children",
    "prompt": "Design philosophy for children discussions with age-appropriate philosophical questions, concept exploration, community of inquiry, and reflective activities for:"
  },
  {
    "id": 194,
    "category": "education",
    "title": "Multilingual Learner Support",
    "prompt": "Design comprehensive language support strategies for multilingual learners with vocabulary scaffolds, comprehensible input, speaking opportunities, and home language connections for:"
  },
  {
    "id": 195,
    "category": "education",
    "title": "Assessment Literacy",
    "prompt": "Design professional learning on assessment literacy covering assessment design, feedback practices, grading reform, and data-driven instruction for:"
  },
  {
    "id": 196,
    "category": "education",
    "title": "Blended Learning Model",
    "prompt": "Design a blended learning model with station rotation, flex model, or flipped approach with technology integration and face-to-face optimization for:"
  },
  {
    "id": 197,
    "category": "education",
    "title": "Trauma-Informed Practice",
    "prompt": "Design trauma-informed educational practices with safety building, relationship development, co-regulation strategies, and resilience building for:"
  },
  {
    "id": 198,
    "category": "creative",
    "title": "Complex Character Creation",
    "prompt": "Create a psychologically rich fictional character with detailed backstory, childhood influences, core wounds, defense mechanisms, contradictory traits, secret desires, relationship patterns, and a compelling character arc for:"
  },
  {
    "id": 199,
    "category": "creative",
    "title": "World Building",
    "prompt": "Build an immersive fictional world with geography, climate systems, history spanning centuries, multiple cultures with distinct languages and customs, political systems, economies, religions, magic or technology systems, and myths for:"
  },
  {
    "id": 200,
    "category": "creative",
    "title": "Dialogue Writing",
    "prompt": "Write natural, subtext-rich dialogue that reveals character through word choice, rhythm, and what's left unsaid, advances plot, and creates tension in this scene:"
  },
  {
    "id": 201,
    "category": "creative",
    "title": "Poetry Collection",
    "prompt": "Write a cohesive collection of 5 poems using different forms (sonnet, free verse, villanelle, haiku sequence, prose poem) united by theme, with rich imagery and emotional depth about:"
  },
  {
    "id": 202,
    "category": "creative",
    "title": "Screenplay Scene",
    "prompt": "Write a professional screenplay scene with precise action lines, authentic dialogue, proper formatting, subtext, visual storytelling, and emotional impact for:"
  },
  {
    "id": 203,
    "category": "creative",
    "title": "Fantasy Magic System",
    "prompt": "Design a complete, internally consistent magic system with rules, costs, limitations, cultural integration, historical origins, and impact on society for:"
  },
  {
    "id": 204,
    "category": "creative",
    "title": "Villain Creation",
    "prompt": "Create a complex, compelling villain with understandable motivations, tragic backstory, genuine menace, philosophical worldview, and relationship to the protagonist for:"
  },
  {
    "id": 205,
    "category": "creative",
    "title": "Story Opening",
    "prompt": "Write 5 different powerful story openings for the same premise using different techniques: in medias res, character voice, atmospheric setting, provocative statement, and sensory immersion for:"
  },
  {
    "id": 206,
    "category": "creative",
    "title": "Genre Mashup",
    "prompt": "Write a story that authentically blends two genres in unexpected ways, creating something fresh while honoring both genre conventions for:"
  },
  {
    "id": 207,
    "category": "creative",
    "title": "Unreliable Narrator",
    "prompt": "Write a first-person narrative with an unreliable narrator where the truth is subtly different from what's being told, with clues embedded throughout for:"
  },
  {
    "id": 208,
    "category": "creative",
    "title": "Flash Fiction",
    "prompt": "Write 5 complete flash fiction pieces (under 500 words each) that pack maximum emotional impact, narrative arc, and meaning for the theme of:"
  },
  {
    "id": 209,
    "category": "creative",
    "title": "Mythological Creation",
    "prompt": "Create an original mythology for a culture with creation myth, pantheon of gods, heroic legends, moral fables, and ritual origins for:"
  },
  {
    "id": 210,
    "category": "creative",
    "title": "Alternate History",
    "prompt": "Write an alternate history story where one historical event changed differently, exploring the realistic ripple effects on culture, technology, and human society for:"
  },
  {
    "id": 211,
    "category": "creative",
    "title": "Epistolary Story",
    "prompt": "Write a story told entirely through letters, emails, texts, journal entries, or documents that reveals a complete narrative arc through:"
  },
  {
    "id": 212,
    "category": "creative",
    "title": "Stream of Consciousness",
    "prompt": "Write a stream of consciousness passage that captures the authentic flow of a character's thoughts, memories, and perceptions during:"
  },
  {
    "id": 213,
    "category": "creative",
    "title": "Satirical Piece",
    "prompt": "Write a sharp satirical piece that uses irony, exaggeration, and dark humor to critique the following subject while remaining clever rather than mean-spirited:"
  },
  {
    "id": 214,
    "category": "creative",
    "title": "Foreshadowing Technique",
    "prompt": "Write a scene with masterfully subtle foreshadowing where every detail serves double duty without telegraphing the ending for:"
  },
  {
    "id": 215,
    "category": "creative",
    "title": "Sensory Writing",
    "prompt": "Write a passage that engages all five senses plus proprioception and emotion to create a fully immersive experience of:"
  },
  {
    "id": 216,
    "category": "creative",
    "title": "Plot Twist Design",
    "prompt": "Design three unexpected but inevitable plot twists that recontextualize everything that came before while remaining completely fair to the reader for:"
  },
  {
    "id": 217,
    "category": "creative",
    "title": "Scene Tension Building",
    "prompt": "Rewrite this low-stakes scene to build unbearable tension through pacing, word choice, physical detail, and subtext while keeping the events identical:"
  },
  {
    "id": 218,
    "category": "creative",
    "title": "Metaphor Development",
    "prompt": "Develop an extended metaphor or central symbol that carries thematic weight throughout an entire narrative for the theme of:"
  },
  {
    "id": 219,
    "category": "creative",
    "title": "Multi-POV Story",
    "prompt": "Write the same event from three different characters' perspectives, showing how each person's background, desires, and biases shape what they perceive for:"
  },
  {
    "id": 220,
    "category": "creative",
    "title": "Short Story Structure",
    "prompt": "Write a complete short story using a non-linear structure (in medias res, frame story, reverse chronology) that enhances rather than obscures the meaning of:"
  },
  {
    "id": 221,
    "category": "creative",
    "title": "Prose Style Experiment",
    "prompt": "Write the same scene in five completely different prose styles: minimalist Carver-esque, maximalist Dickenisian, lyrical, hardboiled, and experimental for:"
  },
  {
    "id": 222,
    "category": "creative",
    "title": "Comic Timing",
    "prompt": "Write a comedic scene with perfect timing, escalation, callback, and misdirection that builds to a satisfying comedic payoff for:"
  },
  {
    "id": 223,
    "category": "creative",
    "title": "Dark Fantasy World",
    "prompt": "Build a grimdark fantasy world that explores moral ambiguity, systemic corruption, and human resilience without losing hope entirely for:"
  },
  {
    "id": 224,
    "category": "creative",
    "title": "Children's Story",
    "prompt": "Write an enchanting children's story with age-appropriate language, repetition, moral lesson embedded naturally, and illustrations description for:"
  },
  {
    "id": 225,
    "category": "creative",
    "title": "Horror Story",
    "prompt": "Write a psychologically terrifying horror story that builds dread through atmosphere and implication rather than gore, subverting genre expectations for:"
  },
  {
    "id": 226,
    "category": "creative",
    "title": "Romance Arc",
    "prompt": "Write a complete slow-burn romance arc with believable chemistry, obstacles, character growth, misunderstanding, and emotionally satisfying resolution for:"
  },
  {
    "id": 227,
    "category": "creative",
    "title": "Science Fiction Concept",
    "prompt": "Explore a hard science fiction concept with scientific accuracy, human implications, social commentary, and compelling narrative for:"
  },
  {
    "id": 228,
    "category": "creative",
    "title": "Fairy Tale Subversion",
    "prompt": "Rewrite a classic fairy tale that completely subverts the original's assumptions while honoring the archetypal patterns it represents for:"
  },
  {
    "id": 229,
    "category": "creative",
    "title": "Voice Development",
    "prompt": "Write three chapters of the same story in three completely different narrative voices to explore how voice shapes meaning for:"
  },
  {
    "id": 230,
    "category": "creative",
    "title": "Symbolic Imagery",
    "prompt": "Write a scene where physical details and actions carry heavy symbolic weight that reinforces the story's themes without becoming heavy-handed for:"
  },
  {
    "id": 231,
    "category": "creative",
    "title": "Emotional Scene Writing",
    "prompt": "Write a scene of intense emotional impact that achieves its effect through restraint, specific detail, and character action rather than explicit statement for:"
  },
  {
    "id": 232,
    "category": "creative",
    "title": "Backstory Integration",
    "prompt": "Write scenes that reveal character backstory naturally through present-day behavior, dialogue triggers, and sensory memories rather than exposition for:"
  },
  {
    "id": 233,
    "category": "creative",
    "title": "World Mythology",
    "prompt": "Create a complete mythological framework with cosmology, divine beings, heroic ages, apocalypse mythology, and how mortals relate to the divine for:"
  },
  {
    "id": 234,
    "category": "creative",
    "title": "Comic Script",
    "prompt": "Write a complete comic book script with panel descriptions, dialogue, pacing, visual storytelling, and cliffhanger ending for:"
  },
  {
    "id": 235,
    "category": "creative",
    "title": "Song Lyrics",
    "prompt": "Write original song lyrics with verse, pre-chorus, chorus, bridge structure, internal rhyme, metaphorical language, and emotional arc for the theme of:"
  },
  {
    "id": 236,
    "category": "creative",
    "title": "Interactive Story",
    "prompt": "Write a branching interactive story with three key decision points, each leading to different outcomes that feel equally meaningful for:"
  },
  {
    "id": 237,
    "category": "creative",
    "title": "Environmental Storytelling",
    "prompt": "Describe a location so richly that the story of what happened there can be read entirely from the physical details without a single character present for:"
  },
  {
    "id": 238,
    "category": "creative",
    "title": "Thematic Essay Creative",
    "prompt": "Write a personal essay that uses a specific concrete experience as a lens to explore a universal theme with literary technique and emotional honesty about:"
  },
  {
    "id": 239,
    "category": "creative",
    "title": "Creative Nonfiction Scene",
    "prompt": "Write a creative nonfiction scene from memory or imagination that uses fictional techniques (scene, dialogue, interiority) to explore truth about:"
  },
  {
    "id": 240,
    "category": "creative",
    "title": "Speculative Fiction",
    "prompt": "Write a near-future speculative fiction piece that extrapolates a current trend to its logical extreme, exploring human consequences for:"
  },
  {
    "id": 241,
    "category": "creative",
    "title": "Magical Realism",
    "prompt": "Write a magical realism story where one impossible element is treated with complete matter-of-fact normalcy while everything else remains realistic for:"
  },
  {
    "id": 242,
    "category": "creative",
    "title": "Character Study",
    "prompt": "Write an extended character study that reveals a complete human being through a single ordinary day, with no dramatic events required for:"
  },
  {
    "id": 243,
    "category": "creative",
    "title": "Found Footage Story",
    "prompt": "Write a found footage narrative (video transcripts, recordings, notes) that tells a complete horror or mystery story entirely through discovered documents about:"
  },
  {
    "id": 244,
    "category": "creative",
    "title": "Experimental Form",
    "prompt": "Write a story that uses an unconventional form (recipe, instruction manual, classified ad, dictionary entries) to tell a complete narrative about:"
  },
  {
    "id": 245,
    "category": "marketing",
    "title": "Facebook Ad Campaign",
    "prompt": "Write a complete Facebook advertising campaign with 5 ad variations, targeting strategy, A/B testing plan, retargeting sequence, and optimization framework for:"
  },
  {
    "id": 246,
    "category": "marketing",
    "title": "Google Ads Strategy",
    "prompt": "Develop a complete Google Ads strategy with campaign structure, keyword research, ad copy variations, bidding strategy, quality score optimization, and conversion tracking for:"
  },
  {
    "id": 247,
    "category": "marketing",
    "title": "Content Marketing Strategy",
    "prompt": "Create a 90-day content marketing strategy with audience personas, content pillars, SEO keyword mapping, editorial calendar, distribution plan, and KPI tracking for:"
  },
  {
    "id": 248,
    "category": "marketing",
    "title": "Email Marketing Sequence",
    "prompt": "Write a complete 7-email nurture sequence with subject lines, preview text, personalization tokens, segmentation triggers, and A/B testing recommendations for:"
  },
  {
    "id": 249,
    "category": "marketing",
    "title": "Social Media Calendar",
    "prompt": "Create a 30-day social media content calendar with platform-specific posts, optimal posting times, hashtag strategy, engagement tactics, and performance metrics for:"
  },
  {
    "id": 250,
    "category": "marketing",
    "title": "Brand Positioning Statement",
    "prompt": "Develop a compelling brand positioning statement with unique value proposition, target audience definition, category framing, key differentiators, and proof points for:"
  },
  {
    "id": 251,
    "category": "marketing",
    "title": "Influencer Marketing Strategy",
    "prompt": "Design a comprehensive influencer marketing strategy with tier selection, outreach templates, brief creation, compensation models, content guidelines, and ROI measurement for:"
  },
  {
    "id": 252,
    "category": "marketing",
    "title": "Video Marketing Plan",
    "prompt": "Create a complete video marketing strategy with content types, production guidelines, distribution channels, optimization tactics, and performance benchmarks for:"
  },
  {
    "id": 253,
    "category": "marketing",
    "title": "SEO Strategy",
    "prompt": "Develop a comprehensive SEO strategy with technical audit, keyword research, content strategy, link building plan, local SEO, and tracking dashboard for:"
  },
  {
    "id": 254,
    "category": "marketing",
    "title": "Product Launch Campaign",
    "prompt": "Design a complete product launch marketing campaign with pre-launch buzz, launch day activities, post-launch momentum, PR strategy, and success metrics for:"
  },
  {
    "id": 255,
    "category": "marketing",
    "title": "Conversion Rate Optimization",
    "prompt": "Design a systematic CRO program with heatmap analysis plan, A/B test roadmap, UX improvements, messaging optimization, and testing methodology for:"
  },
  {
    "id": 256,
    "category": "marketing",
    "title": "Customer Acquisition Strategy",
    "prompt": "Develop a multi-channel customer acquisition strategy with channel mix, CAC targets, creative strategy, landing page optimization, and scaling framework for:"
  },
  {
    "id": 257,
    "category": "marketing",
    "title": "Referral Program",
    "prompt": "Design a viral referral program with incentive structure, referral mechanics, sharing triggers, reward fulfillment, and fraud prevention for:"
  },
  {
    "id": 258,
    "category": "marketing",
    "title": "Community Marketing",
    "prompt": "Design a community-led marketing strategy with platform selection, community programming, ambassador program, user-generated content, and measurement framework for:"
  },
  {
    "id": 259,
    "category": "marketing",
    "title": "Account-Based Marketing",
    "prompt": "Develop an ABM strategy with account selection criteria, personalized campaign design, sales alignment, multi-channel orchestration, and pipeline influence measurement for:"
  },
  {
    "id": 260,
    "category": "marketing",
    "title": "PR Strategy",
    "prompt": "Develop a comprehensive PR strategy with media landscape analysis, story angles, press release templates, journalist targeting, crisis preparation, and coverage tracking for:"
  },
  {
    "id": 261,
    "category": "marketing",
    "title": "Podcast Marketing",
    "prompt": "Develop a podcast marketing strategy with show concept, guest strategy, distribution, monetization, cross-promotion, and listener growth tactics for:"
  },
  {
    "id": 262,
    "category": "marketing",
    "title": "Event Marketing",
    "prompt": "Design a complete event marketing strategy with pre-event promotion, registration optimization, attendee experience, content capture, and post-event nurture for:"
  },
  {
    "id": 263,
    "category": "marketing",
    "title": "Retargeting Strategy",
    "prompt": "Design a sophisticated retargeting strategy with audience segmentation, creative sequencing, frequency capping, cross-platform coordination, and attribution for:"
  },
  {
    "id": 264,
    "category": "marketing",
    "title": "Growth Hacking Experiments",
    "prompt": "Design 20 growth hacking experiments with hypothesis, test design, success metrics, implementation requirements, and expected impact for:"
  },
  {
    "id": 265,
    "category": "marketing",
    "title": "Customer Lifetime Value",
    "prompt": "Develop a CLV optimization strategy with segmentation, personalization program, win-back campaigns, upsell/cross-sell, and loyalty mechanics for:"
  },
  {
    "id": 266,
    "category": "marketing",
    "title": "Marketing Attribution Model",
    "prompt": "Design a comprehensive marketing attribution model with touchpoint mapping, attribution methodology, data requirements, reporting structure, and optimization process for:"
  },
  {
    "id": 267,
    "category": "marketing",
    "title": "Demand Generation",
    "prompt": "Create a complete demand generation strategy with awareness tactics, lead generation programs, nurture infrastructure, sales handoff, and revenue attribution for:"
  },
  {
    "id": 268,
    "category": "marketing",
    "title": "Brand Awareness Campaign",
    "prompt": "Design a brand awareness campaign with reach strategy, creative concept, channel mix, frequency planning, measurement approach, and brand lift methodology for:"
  },
  {
    "id": 269,
    "category": "marketing",
    "title": "Local Marketing Strategy",
    "prompt": "Develop a comprehensive local marketing strategy with Google Business Profile optimization, local SEO, community partnerships, event marketing, and hyperlocal advertising for:"
  },
  {
    "id": 270,
    "category": "marketing",
    "title": "E-commerce Marketing",
    "prompt": "Create a complete e-commerce marketing strategy with product page optimization, cart abandonment, post-purchase sequence, seasonal campaigns, and marketplace strategy for:"
  },
  {
    "id": 271,
    "category": "marketing",
    "title": "SaaS Marketing Playbook",
    "prompt": "Develop a complete SaaS marketing playbook with free trial optimization, activation campaigns, expansion revenue, churn prevention, and product-led growth tactics for:"
  },
  {
    "id": 272,
    "category": "marketing",
    "title": "Guerrilla Marketing",
    "prompt": "Design 10 creative guerrilla marketing campaigns that generate massive attention on minimal budget for:"
  },
  {
    "id": 273,
    "category": "marketing",
    "title": "Marketing Automation",
    "prompt": "Design a comprehensive marketing automation architecture with trigger logic, content mapping, lead scoring, CRM integration, and performance reporting for:"
  },
  {
    "id": 274,
    "category": "marketing",
    "title": "Competitive Positioning",
    "prompt": "Develop a competitive positioning strategy with battlecards, differentiation messaging, objection handling, win/loss analysis, and sales enablement for:"
  },
  {
    "id": 275,
    "category": "marketing",
    "title": "Customer Advocacy Program",
    "prompt": "Design a customer advocacy program with advocate identification, nurture track, case study development, speaking opportunities, and reference management for:"
  },
  {
    "id": 276,
    "category": "marketing",
    "title": "Mobile Marketing Strategy",
    "prompt": "Develop a mobile marketing strategy with app store optimization, push notification strategy, in-app messaging, SMS marketing, and mobile-first content for:"
  },
  {
    "id": 277,
    "category": "marketing",
    "title": "Seasonal Marketing Calendar",
    "prompt": "Create a comprehensive seasonal marketing calendar with campaign themes, timing, offers, creative direction, and channel activation for:"
  },
  {
    "id": 278,
    "category": "marketing",
    "title": "LinkedIn Marketing Strategy",
    "prompt": "Develop a complete LinkedIn marketing strategy with company page optimization, thought leadership content, sponsored content, InMail campaigns, and sales navigator for:"
  },
  {
    "id": 279,
    "category": "marketing",
    "title": "Podcast Advertising",
    "prompt": "Create a complete podcast advertising strategy with show selection, ad format, host-read scripts, tracking methodology, and optimization process for:"
  },
  {
    "id": 280,
    "category": "marketing",
    "title": "Affiliate Marketing Program",
    "prompt": "Design a high-performance affiliate program with commission structure, partner recruitment, creative assets, compliance guidelines, and performance optimization for:"
  },
  {
    "id": 281,
    "category": "marketing",
    "title": "Customer Onboarding Marketing",
    "prompt": "Design a marketing-driven onboarding experience that activates new customers, drives early value, reduces churn, and creates expansion opportunities for:"
  },
  {
    "id": 282,
    "category": "marketing",
    "title": "Social Commerce Strategy",
    "prompt": "Develop a social commerce strategy with shoppable content, live shopping, social proof, influencer product seeding, and conversion optimization for:"
  },
  {
    "id": 283,
    "category": "marketing",
    "title": "Brand Storytelling",
    "prompt": "Develop a brand storytelling framework with origin story, customer hero narratives, values in action stories, and content distribution strategy for:"
  },
  {
    "id": 284,
    "category": "marketing",
    "title": "Marketing Metrics Dashboard",
    "prompt": "Design a comprehensive marketing metrics dashboard with leading indicators, lagging indicators, attribution data, trending analysis, and executive summary for:"
  },
  {
    "id": 285,
    "category": "marketing",
    "title": "Niche Marketing Strategy",
    "prompt": "Develop a hyper-targeted niche marketing strategy with micro-segmentation, specialized messaging, community infiltration, and category ownership tactics for:"
  },
  {
    "id": 286,
    "category": "marketing",
    "title": "Subscription Marketing",
    "prompt": "Develop a subscription marketing strategy with trial optimization, payment page, dunning management, pause vs cancel, and win-back campaigns for:"
  },
  {
    "id": 287,
    "category": "marketing",
    "title": "International Marketing",
    "prompt": "Develop an international marketing expansion strategy with market prioritization, localization requirements, channel adaptation, and cultural sensitivity guidelines for:"
  },
  {
    "id": 288,
    "category": "marketing",
    "title": "User-Generated Content",
    "prompt": "Design a UGC strategy with content encouragement mechanics, curation process, rights management, distribution plan, and performance tracking for:"
  },
  {
    "id": 289,
    "category": "marketing",
    "title": "Thought Leadership Marketing",
    "prompt": "Design a thought leadership marketing program with content themes, publication strategy, speaking circuit, research reports, and authority building for:"
  },
  {
    "id": 290,
    "category": "marketing",
    "title": "Omnichannel Marketing",
    "prompt": "Design a seamless omnichannel marketing experience with touchpoint mapping, message sequencing, channel handoffs, unified measurement, and personalization for:"
  },
  {
    "id": 291,
    "category": "marketing",
    "title": "Marketing Budget Allocation",
    "prompt": "Develop a data-driven marketing budget allocation framework with channel ROI analysis, portfolio optimization, scenario planning, and reallocation triggers for:"
  },
  {
    "id": 292,
    "category": "marketing",
    "title": "Crisis Communication",
    "prompt": "Develop a crisis communication plan with response protocols, messaging frameworks, stakeholder communication, media handling, and reputation recovery for:"
  },
  {
    "id": 293,
    "category": "marketing",
    "title": "Customer Feedback Marketing",
    "prompt": "Design a voice-of-customer program that turns customer insights into marketing advantages with research methods, analysis, and activation strategy for:"
  },
  {
    "id": 294,
    "category": "marketing",
    "title": "Viral Marketing Campaign",
    "prompt": "Design a viral marketing campaign with shareable mechanics, emotional triggers, social currency, practical value, and amplification strategy for:"
  },
  {
    "id": 295,
    "category": "productivity",
    "title": "Personal Productivity System",
    "prompt": "Design a comprehensive personal productivity system combining time blocking, task management, energy management, weekly review, and continuous improvement for someone who:"
  },
  {
    "id": 296,
    "category": "productivity",
    "title": "Morning Routine Design",
    "prompt": "Design an optimized morning routine with sleep wake time, movement, mindfulness, nutrition, learning, and planning blocks based on neuroscience and high-performance research for:"
  },
  {
    "id": 297,
    "category": "productivity",
    "title": "Deep Work Schedule",
    "prompt": "Create a deep work schedule with protected focus blocks, distraction elimination protocols, environment design, recovery periods, and weekly review for:"
  },
  {
    "id": 298,
    "category": "productivity",
    "title": "Goal Setting Framework",
    "prompt": "Design a comprehensive goal setting system with life area mapping, 10-year vision, annual goals, quarterly rocks, weekly priorities, and daily habits for:"
  },
  {
    "id": 299,
    "category": "productivity",
    "title": "Time Audit Process",
    "prompt": "Design a complete time audit process with time tracking methodology, analysis framework, time wasters identification, and redesigned calendar for:"
  },
  {
    "id": 300,
    "category": "productivity",
    "title": "Meeting Optimization",
    "prompt": "Design a meeting culture overhaul with meeting types, time budgets, agenda templates, facilitation guides, decision protocols, and async alternatives for:"
  },
  {
    "id": 301,
    "category": "productivity",
    "title": "Email Management System",
    "prompt": "Design a zero-inbox email system with triage process, folder structure, template library, unsubscribe protocol, and response time standards for:"
  },
  {
    "id": 302,
    "category": "productivity",
    "title": "Note-Taking System",
    "prompt": "Design a comprehensive note-taking system combining capture, processing, linking, retrieval, and review using Zettelkasten or PARA methodology for:"
  },
  {
    "id": 303,
    "category": "productivity",
    "title": "Decision-Making Framework",
    "prompt": "Create a decision-making framework with decision types, information gathering, stakeholder input, options analysis, commitment, and review process for:"
  },
  {
    "id": 304,
    "category": "productivity",
    "title": "Weekly Review Process",
    "prompt": "Design a comprehensive weekly review process with reflection questions, metrics review, task capture, calendar planning, and intention setting for:"
  },
  {
    "id": 305,
    "category": "productivity",
    "title": "Habit Stacking System",
    "prompt": "Design a habit stacking system with anchor habits, implementation intentions, environment design, tracking, and adjustment process for:"
  },
  {
    "id": 306,
    "category": "productivity",
    "title": "Energy Management",
    "prompt": "Design an energy management system covering sleep optimization, nutrition timing, exercise scheduling, mental recovery, and ultradian rhythms for:"
  },
  {
    "id": 307,
    "category": "productivity",
    "title": "Focus Enhancement",
    "prompt": "Design a focus enhancement protocol with environment optimization, digital minimalism, attention training, break structure, and recovery practices for:"
  },
  {
    "id": 308,
    "category": "productivity",
    "title": "Project Management System",
    "prompt": "Design a personal project management system with project capture, breakdown, scheduling, progress tracking, and completion review for:"
  },
  {
    "id": 309,
    "category": "productivity",
    "title": "Reading System",
    "prompt": "Design a comprehensive reading system with book selection, active reading techniques, note-taking, review schedule, and knowledge application for:"
  },
  {
    "id": 310,
    "category": "productivity",
    "title": "Learning Acceleration",
    "prompt": "Design a rapid learning protocol using spaced repetition, interleaving, retrieval practice, elaborative interrogation, and feedback loops for:"
  },
  {
    "id": 311,
    "category": "productivity",
    "title": "Delegation Framework",
    "prompt": "Design a delegation framework with task assessment, delegation decision tree, handoff protocol, progress monitoring, and feedback system for:"
  },
  {
    "id": 312,
    "category": "productivity",
    "title": "Automation Strategy",
    "prompt": "Design a personal automation strategy identifying repetitive tasks, tool selection, workflow design, testing, and maintenance for:"
  },
  {
    "id": 313,
    "category": "productivity",
    "title": "Distraction Management",
    "prompt": "Design a comprehensive distraction management system covering digital, environmental, social, and internal distractions with specific protocols for each:"
  },
  {
    "id": 314,
    "category": "productivity",
    "title": "Creative Process",
    "prompt": "Design a structured creative process with idea generation, incubation, elaboration, evaluation, and implementation phases for:"
  },
  {
    "id": 315,
    "category": "productivity",
    "title": "Stress Management System",
    "prompt": "Design a comprehensive stress management system with early warning signs, immediate interventions, recovery practices, and systemic changes for:"
  },
  {
    "id": 316,
    "category": "productivity",
    "title": "Work-Life Integration",
    "prompt": "Design a work-life integration framework with boundary setting, role clarity, transition rituals, recovery activities, and regular rebalancing for:"
  },
  {
    "id": 317,
    "category": "productivity",
    "title": "Professional Development Plan",
    "prompt": "Design a comprehensive professional development plan with skill gap analysis, learning resources, practice opportunities, mentorship, and progress tracking for:"
  },
  {
    "id": 318,
    "category": "productivity",
    "title": "Accountability System",
    "prompt": "Design a personal accountability system with goal tracking, accountability partners, review cadence, consequence structures, and course correction protocols for:"
  },
  {
    "id": 319,
    "category": "productivity",
    "title": "Inbox Zero Protocol",
    "prompt": "Design a complete communications management protocol for email, Slack, and other tools to maintain clarity and prevent overwhelm for:"
  },
  {
    "id": 320,
    "category": "productivity",
    "title": "Content Creation System",
    "prompt": "Design a systematic content creation workflow from ideation to publishing with batching, templates, repurposing, and quality control for:"
  },
  {
    "id": 321,
    "category": "productivity",
    "title": "Financial Organization",
    "prompt": "Design a complete personal financial organization system with account structure, budgeting method, investment tracking, insurance review, and annual audit for:"
  },
  {
    "id": 322,
    "category": "productivity",
    "title": "Health Optimization Protocol",
    "prompt": "Design a comprehensive health optimization protocol covering sleep, nutrition, exercise, stress, relationships, and preventive care for:"
  },
  {
    "id": 323,
    "category": "productivity",
    "title": "Social Media Productivity",
    "prompt": "Design a social media productivity system that maintains presence, builds network, and consumes strategically without time waste for:"
  },
  {
    "id": 324,
    "category": "productivity",
    "title": "Remote Work Optimization",
    "prompt": "Design a remote work optimization system with workspace setup, schedule structure, communication protocols, social connection, and performance tracking for:"
  },
  {
    "id": 325,
    "category": "productivity",
    "title": "Strategic Thinking Practice",
    "prompt": "Design a strategic thinking practice with regular reflection time, horizon planning, scenario thinking, and decision quality review for:"
  },
  {
    "id": 326,
    "category": "productivity",
    "title": "Personal Brand Building",
    "prompt": "Design a systematic personal brand building plan with positioning, content strategy, network building, speaking, and online presence optimization for:"
  },
  {
    "id": 327,
    "category": "productivity",
    "title": "Mentorship Program",
    "prompt": "Design a comprehensive mentorship system with mentor identification, relationship structure, meeting agenda, feedback protocols, and value exchange for:"
  },
  {
    "id": 328,
    "category": "productivity",
    "title": "Annual Review Process",
    "prompt": "Design a comprehensive annual review process covering all life areas, achievements analysis, lessons learned, values alignment, and next year planning for:"
  },
  {
    "id": 329,
    "category": "productivity",
    "title": "Collaboration Systems",
    "prompt": "Design effective collaboration systems for remote teams with documentation standards, communication protocols, decision making, and relationship building for:"
  },
  {
    "id": 330,
    "category": "productivity",
    "title": "Mind Mapping Practice",
    "prompt": "Design a mind mapping practice for problem solving, planning, learning, and creativity with templates, tools, and integration into workflow for:"
  },
  {
    "id": 331,
    "category": "productivity",
    "title": "Journaling System",
    "prompt": "Design a comprehensive journaling system with morning pages, gratitude practice, reflection prompts, future self letters, and review rituals for:"
  },
  {
    "id": 332,
    "category": "productivity",
    "title": "Networking Strategy",
    "prompt": "Design a systematic networking strategy with relationship mapping, outreach templates, follow-up system, value-giving approach, and event strategy for:"
  },
  {
    "id": 333,
    "category": "productivity",
    "title": "Creative Block Breakthrough",
    "prompt": "Design a creative block breakthrough protocol with diagnostic questions, unblocking exercises, environmental changes, and momentum building strategies for:"
  },
  {
    "id": 334,
    "category": "productivity",
    "title": "Personal Knowledge Management",
    "prompt": "Design a personal knowledge management system with capture tools, processing workflow, linking strategy, retrieval system, and knowledge application for:"
  },
  {
    "id": 335,
    "category": "productivity",
    "title": "Cognitive Performance",
    "prompt": "Design a cognitive performance optimization protocol covering nutrition, sleep, exercise, stress, social connection, and cognitive training for:"
  },
  {
    "id": 336,
    "category": "productivity",
    "title": "Task Batching System",
    "prompt": "Design a task batching system that groups similar activities, creates flow states, reduces switching costs, and maximizes output quality for:"
  },
  {
    "id": 337,
    "category": "productivity",
    "title": "Feedback System",
    "prompt": "Design a personal feedback system for soliciting, processing, integrating, and acting on feedback from multiple sources for:"
  },
  {
    "id": 338,
    "category": "productivity",
    "title": "Mindfulness Practice",
    "prompt": "Design a mindfulness practice program with formal meditation, informal practice, stress response training, and workplace integration for:"
  },
  {
    "id": 339,
    "category": "productivity",
    "title": "Career Management",
    "prompt": "Design a proactive career management system with industry monitoring, skill development, visibility building, opportunity creation, and transition planning for:"
  },
  {
    "id": 340,
    "category": "productivity",
    "title": "Relationship Management",
    "prompt": "Design a personal relationship management system with contact organization, regular touchpoints, meaningful gestures, and relationship health monitoring for:"
  },
  {
    "id": 341,
    "category": "productivity",
    "title": "Digital Organization",
    "prompt": "Design a comprehensive digital organization system for files, photos, passwords, subscriptions, and digital assets with naming conventions and maintenance schedule for:"
  },
  {
    "id": 342,
    "category": "productivity",
    "title": "Resilience Building",
    "prompt": "Design a personal resilience building program with adversity response training, support systems, recovery practices, and post-traumatic growth for:"
  },
  {
    "id": 343,
    "category": "productivity",
    "title": "Life Design",
    "prompt": "Design a comprehensive life design process with values clarification, life area assessment, ideal life vision, experiment design, and iteration process for:"
  },
  {
    "id": 344,
    "category": "health",
    "title": "Personalized Workout Plan",
    "prompt": "Design a science-based workout plan with progressive overload, exercise selection, sets/reps/tempo, rest periods, deload weeks, and tracking system for a person who:"
  },
  {
    "id": 345,
    "category": "health",
    "title": "Nutrition Plan",
    "prompt": "Design a comprehensive nutrition plan with calorie targets, macronutrient ratios, meal timing, food choices, meal prep strategy, and supplementation for someone who:"
  },
  {
    "id": 346,
    "category": "health",
    "title": "Sleep Optimization",
    "prompt": "Design a complete sleep optimization protocol covering sleep hygiene, bedroom environment, pre-sleep routine, sleep schedule, and troubleshooting common sleep problems for:"
  },
  {
    "id": 347,
    "category": "health",
    "title": "Stress Reduction Program",
    "prompt": "Design a comprehensive stress reduction program combining breathing techniques, progressive muscle relaxation, mindfulness, lifestyle changes, and professional support for:"
  },
  {
    "id": 348,
    "category": "health",
    "title": "Mobility and Flexibility",
    "prompt": "Design a comprehensive mobility and flexibility program with dynamic warm-up, static stretching, PNF techniques, yoga flows, and recovery protocols for:"
  },
  {
    "id": 349,
    "category": "health",
    "title": "Mental Health Maintenance",
    "prompt": "Design a mental health maintenance program with mood tracking, social connection, purpose cultivation, professional support structure, and crisis plan for:"
  },
  {
    "id": 350,
    "category": "health",
    "title": "Weight Management",
    "prompt": "Design a sustainable weight management strategy with realistic goals, behavioral changes, nutrition approach, exercise plan, habit formation, and plateau strategies for:"
  },
  {
    "id": 351,
    "category": "health",
    "title": "Athletic Performance",
    "prompt": "Design a complete athletic performance optimization program with periodization, sport-specific training, nutrition timing, recovery protocols, and peak performance for:"
  },
  {
    "id": 352,
    "category": "health",
    "title": "Chronic Pain Management",
    "prompt": "Design a comprehensive chronic pain management approach combining movement therapy, lifestyle modifications, pain neuroscience education, and psychological strategies for:"
  },
  {
    "id": 353,
    "category": "health",
    "title": "Immune System Optimization",
    "prompt": "Design a science-backed immune system optimization protocol covering nutrition, sleep, exercise, stress management, and environmental factors for:"
  },
  {
    "id": 354,
    "category": "health",
    "title": "Gut Health Protocol",
    "prompt": "Design a comprehensive gut health optimization protocol with dietary changes, probiotic strategy, stress management, sleep, and specific interventions for:"
  },
  {
    "id": 355,
    "category": "health",
    "title": "Hormone Balance",
    "prompt": "Design a lifestyle protocol for supporting healthy hormone balance covering nutrition, exercise, sleep, stress, environmental toxins, and medical monitoring for:"
  },
  {
    "id": 356,
    "category": "health",
    "title": "Cardiovascular Health",
    "prompt": "Design a comprehensive cardiovascular health program with aerobic training, HIIT, nutrition, stress management, sleep, and monitoring protocols for:"
  },
  {
    "id": 357,
    "category": "health",
    "title": "Longevity Protocol",
    "prompt": "Design a science-based longevity protocol incorporating exercise, nutrition, sleep, stress management, social connection, and cognitive stimulation for:"
  },
  {
    "id": 358,
    "category": "health",
    "title": "Intermittent Fasting",
    "prompt": "Design a personalized intermittent fasting protocol with fasting window selection, eating window optimization, exercise timing, and common challenge solutions for:"
  },
  {
    "id": 359,
    "category": "health",
    "title": "Post-Workout Recovery",
    "prompt": "Design a comprehensive post-workout recovery system with nutrition timing, sleep prioritization, active recovery, cold and heat therapy, and monitoring for:"
  },
  {
    "id": 360,
    "category": "health",
    "title": "Posture Correction",
    "prompt": "Design a posture correction program with assessment, corrective exercises, ergonomic setup, movement habits, and long-term maintenance for:"
  },
  {
    "id": 361,
    "category": "health",
    "title": "Breathing Optimization",
    "prompt": "Design a comprehensive breathing optimization program with assessment, techniques for different contexts, training protocol, and integration into daily life for:"
  },
  {
    "id": 362,
    "category": "health",
    "title": "Mindful Eating",
    "prompt": "Design a mindful eating program with awareness practices, hunger/fullness cues, emotional eating strategies, food relationships, and sustainable habits for:"
  },
  {
    "id": 363,
    "category": "health",
    "title": "Injury Prevention",
    "prompt": "Design a comprehensive injury prevention program for athletes covering movement screening, corrective exercises, load management, recovery, and return-to-sport for:"
  },
  {
    "id": 364,
    "category": "health",
    "title": "Meditation Practice",
    "prompt": "Design a progressive meditation practice program from beginner to advanced with different techniques, retreat recommendations, and daily integration for:"
  },
  {
    "id": 365,
    "category": "health",
    "title": "Detox Protocol",
    "prompt": "Design a science-based detox support protocol focusing on supporting the body's natural detoxification pathways through nutrition, lifestyle, and supplements for:"
  },
  {
    "id": 366,
    "category": "health",
    "title": "Hormonal Health for Women",
    "prompt": "Design a comprehensive hormonal health protocol for women covering cycle tracking, nutrition cycling, exercise programming, stress management, and common conditions for:"
  },
  {
    "id": 367,
    "category": "health",
    "title": "Building Muscle",
    "prompt": "Design a hypertrophy training program with optimal volume, frequency, exercise selection, progressive overload, nutrition support, and recovery for:"
  },
  {
    "id": 368,
    "category": "health",
    "title": "Endurance Training",
    "prompt": "Design a periodized endurance training plan with base building, intensity blocks, race preparation, nutrition strategy, and recovery for:"
  },
  {
    "id": 369,
    "category": "health",
    "title": "Back Pain Relief",
    "prompt": "Design a comprehensive back pain relief program with movement assessment, therapeutic exercises, lifestyle modifications, ergonomics, and prevention strategies for:"
  },
  {
    "id": 370,
    "category": "health",
    "title": "Cognitive Health",
    "prompt": "Design a cognitive health optimization program covering brain training, physical exercise, nutrition, sleep, social engagement, and lifelong learning for:"
  },
  {
    "id": 371,
    "category": "health",
    "title": "Anti-Inflammatory Protocol",
    "prompt": "Design a comprehensive anti-inflammatory lifestyle protocol covering diet, exercise, sleep, stress management, and environmental modifications for:"
  },
  {
    "id": 372,
    "category": "health",
    "title": "Plant-Based Nutrition",
    "prompt": "Design a complete plant-based nutrition strategy ensuring adequate protein, B12, iron, zinc, omega-3, calcium, and vitamin D through food and supplements for:"
  },
  {
    "id": 373,
    "category": "health",
    "title": "Performance Nutrition",
    "prompt": "Design a performance nutrition protocol with pre-workout, intra-workout, post-workout nutrition, hydration strategy, and competition day nutrition for:"
  },
  {
    "id": 374,
    "category": "health",
    "title": "Addiction Recovery Support",
    "prompt": "Design a lifestyle support program for addiction recovery covering daily structure, social support, stress management, purpose building, and relapse prevention for:"
  },
  {
    "id": 375,
    "category": "health",
    "title": "Anxiety Management",
    "prompt": "Design a comprehensive anxiety management program combining CBT techniques, lifestyle changes, relaxation practices, exposure hierarchy, and professional support for:"
  },
  {
    "id": 376,
    "category": "health",
    "title": "Depression Support",
    "prompt": "Design a lifestyle-based depression support protocol with behavioral activation, exercise, nutrition, sleep, social connection, and professional treatment integration for:"
  },
  {
    "id": 377,
    "category": "health",
    "title": "Metabolic Health",
    "prompt": "Design a metabolic health optimization protocol covering blood sugar management, insulin sensitivity, body composition, and cardiovascular risk factors through lifestyle for:"
  },
  {
    "id": 378,
    "category": "health",
    "title": "Bone Health",
    "prompt": "Design a comprehensive bone health program for osteoporosis prevention and treatment covering exercise, nutrition, lifestyle, and medical monitoring for:"
  },
  {
    "id": 379,
    "category": "health",
    "title": "Eye Health",
    "prompt": "Design a complete eye health protocol covering nutrition, blue light management, eye exercises, regular screenings, and lifestyle factors for:"
  },
  {
    "id": 380,
    "category": "health",
    "title": "Skin Health",
    "prompt": "Design a comprehensive skin health protocol from the inside out covering nutrition, hydration, sleep, stress management, and topical care routines for:"
  },
  {
    "id": 381,
    "category": "health",
    "title": "Hearing Health",
    "prompt": "Design a hearing protection and maintenance protocol covering noise exposure management, nutrition, cardiovascular health, and monitoring for:"
  },
  {
    "id": 382,
    "category": "health",
    "title": "Thyroid Health",
    "prompt": "Design a lifestyle optimization protocol for thyroid health covering nutrition, stress management, sleep, toxin reduction, and monitoring for:"
  },
  {
    "id": 383,
    "category": "health",
    "title": "Autoimmune Protocol",
    "prompt": "Design a comprehensive lifestyle protocol for autoimmune condition management covering elimination diet, stress reduction, sleep, gentle exercise, and emotional health for:"
  },
  {
    "id": 384,
    "category": "health",
    "title": "Children's Health",
    "prompt": "Design an age-appropriate health optimization plan covering nutrition, physical activity, sleep, screen time, social development, and preventive care for a child who:"
  },
  {
    "id": 385,
    "category": "health",
    "title": "Healthy Aging",
    "prompt": "Design a comprehensive healthy aging protocol for adults over 60 covering strength training, balance, cognitive health, nutrition, social connection, and preventive care for:"
  },
  {
    "id": 386,
    "category": "health",
    "title": "Fertility Optimization",
    "prompt": "Design a lifestyle optimization protocol for fertility support covering nutrition, weight management, stress reduction, sleep, toxin avoidance, and timing for:"
  },
  {
    "id": 387,
    "category": "health",
    "title": "Pregnancy Wellness",
    "prompt": "Design a comprehensive pregnancy wellness plan covering nutrition, safe exercise, sleep, stress management, prenatal care, and birth preparation for:"
  },
  {
    "id": 388,
    "category": "health",
    "title": "Postpartum Recovery",
    "prompt": "Design a holistic postpartum recovery plan covering physical healing, nutrition, sleep strategy, emotional health, relationship adjustment, and gradual return to fitness for:"
  },
  {
    "id": 389,
    "category": "health",
    "title": "Corporate Wellness",
    "prompt": "Design a comprehensive corporate wellness program covering physical health, mental health, financial wellness, social connection, and work environment optimization for:"
  },
  {
    "id": 390,
    "category": "health",
    "title": "Youth Athletics",
    "prompt": "Design a youth athletic development program covering fundamental movement skills, sport specialization timing, injury prevention, psychological development, and parent education for:"
  },
  {
    "id": 391,
    "category": "health",
    "title": "Senior Fitness",
    "prompt": "Design a safe, effective fitness program for seniors covering strength, balance, flexibility, cardiovascular health, and fall prevention with appropriate progressions for:"
  },
  {
    "id": 392,
    "category": "health",
    "title": "Occupational Health",
    "prompt": "Design an occupational health strategy for someone in a sedentary/physical demanding job covering ergonomics, movement breaks, injury prevention, and mental health for:"
  },
  {
    "id": 393,
    "category": "finance",
    "title": "Personal Budget",
    "prompt": "Create a comprehensive personal budget with income tracking, fixed and variable expenses, savings allocation, investment contributions, emergency fund plan, and monthly review process for someone earning:"
  },
  {
    "id": 394,
    "category": "finance",
    "title": "Investment Portfolio",
    "prompt": "Design a diversified investment portfolio strategy with asset allocation, specific investment vehicles, rebalancing protocol, tax efficiency, and long-term projections for:"
  },
  {
    "id": 395,
    "category": "finance",
    "title": "Debt Elimination",
    "prompt": "Create an aggressive debt elimination strategy using avalanche and snowball methods with payoff timeline, celebration milestones, and behavior change support for:"
  },
  {
    "id": 396,
    "category": "finance",
    "title": "Retirement Planning",
    "prompt": "Design a comprehensive retirement planning strategy with savings rate, account types, investment allocation, Social Security optimization, and withdrawal strategy for:"
  },
  {
    "id": 397,
    "category": "finance",
    "title": "Tax Optimization",
    "prompt": "Develop a comprehensive tax optimization strategy covering account types, deductions, timing strategies, business structures, and charitable giving for:"
  },
  {
    "id": 398,
    "category": "finance",
    "title": "Emergency Fund",
    "prompt": "Design a complete emergency fund strategy with target amount, savings vehicle, contribution plan, replenishment protocol, and what constitutes a true emergency for:"
  },
  {
    "id": 399,
    "category": "finance",
    "title": "Real Estate Investment",
    "prompt": "Develop a real estate investment strategy with market analysis, property evaluation, financing options, cash flow analysis, property management, and portfolio building for:"
  },
  {
    "id": 400,
    "category": "finance",
    "title": "Stock Market Strategy",
    "prompt": "Design a stock market investment strategy with investment philosophy, stock selection criteria, portfolio construction, position sizing, and risk management for:"
  },
  {
    "id": 401,
    "category": "finance",
    "title": "Financial Independence",
    "prompt": "Create a complete financial independence roadmap with savings rate optimization, investment strategy, expense reduction, income growth, and FIRE number calculation for:"
  },
  {
    "id": 402,
    "category": "finance",
    "title": "Business Financial Planning",
    "prompt": "Create a comprehensive business financial plan with revenue forecasting, expense budgeting, cash flow management, capital allocation, and financial KPIs for:"
  },
  {
    "id": 403,
    "category": "finance",
    "title": "Cryptocurrency Strategy",
    "prompt": "Develop a measured cryptocurrency investment strategy with portfolio allocation, coin selection criteria, security practices, tax implications, and risk management for:"
  },
  {
    "id": 404,
    "category": "finance",
    "title": "Insurance Optimization",
    "prompt": "Design a comprehensive insurance optimization strategy covering life, health, disability, property, liability, and specialty coverage with gap analysis for:"
  },
  {
    "id": 405,
    "category": "finance",
    "title": "Estate Planning",
    "prompt": "Create a comprehensive estate planning checklist covering will, trusts, beneficiary designations, power of attorney, healthcare directive, and asset transfer strategy for:"
  },
  {
    "id": 406,
    "category": "finance",
    "title": "Side Income Generation",
    "prompt": "Design a comprehensive strategy for generating side income through freelancing, investments, rental income, digital products, or business ventures for someone who:"
  },
  {
    "id": 407,
    "category": "finance",
    "title": "Credit Score Improvement",
    "prompt": "Design a systematic credit score improvement plan with score analysis, negative item disputes, payment optimization, credit utilization, and new credit strategy for:"
  },
  {
    "id": 408,
    "category": "finance",
    "title": "Financial Goal Setting",
    "prompt": "Design a financial goal setting framework with short, medium, and long-term goals, prioritization methodology, milestone tracking, and accountability system for:"
  },
  {
    "id": 409,
    "category": "finance",
    "title": "Frugality Strategy",
    "prompt": "Design a strategic frugality system that cuts expenses intelligently without sacrificing quality of life, focusing on the highest-impact areas for:"
  },
  {
    "id": 410,
    "category": "finance",
    "title": "Investment Psychology",
    "prompt": "Design a behavioral finance improvement program addressing common investor biases, emotional triggers, decision frameworks, and accountability systems for:"
  },
  {
    "id": 411,
    "category": "finance",
    "title": "Passive Income Blueprint",
    "prompt": "Create a comprehensive passive income blueprint with multiple income streams, startup requirements, scaling strategy, and realistic income projections for:"
  },
  {
    "id": 412,
    "category": "finance",
    "title": "Financial Education Plan",
    "prompt": "Design a financial literacy education plan covering budgeting, investing, taxes, insurance, debt, and wealth building with resources and milestones for:"
  },
  {
    "id": 413,
    "category": "finance",
    "title": "401k Optimization",
    "prompt": "Design a complete 401k optimization strategy with contribution rate, fund selection, rebalancing, employer match maximization, and Roth conversion analysis for:"
  },
  {
    "id": 414,
    "category": "finance",
    "title": "Home Buying Strategy",
    "prompt": "Create a comprehensive home buying strategy with affordability analysis, mortgage types, down payment saving, neighborhood research, offer strategy, and closing process for:"
  },
  {
    "id": 415,
    "category": "finance",
    "title": "Starting a Business Financially",
    "prompt": "Design a complete financial startup plan with initial capital requirements, funding sources, cash flow projections, break-even analysis, and financial milestones for:"
  },
  {
    "id": 416,
    "category": "finance",
    "title": "Wealth Building Roadmap",
    "prompt": "Create a comprehensive wealth building roadmap with income optimization, expense management, investment strategy, tax efficiency, and generational wealth building for:"
  },
  {
    "id": 417,
    "category": "finance",
    "title": "Financial Resilience",
    "prompt": "Design a financial resilience plan with emergency fund, income diversification, insurance coverage, debt management, and stress-testing various scenarios for:"
  },
  {
    "id": 418,
    "category": "finance",
    "title": "Kids and Money",
    "prompt": "Design a comprehensive financial education program for children with age-appropriate money lessons, allowance system, savings habits, and investing introduction for:"
  },
  {
    "id": 419,
    "category": "finance",
    "title": "Divorce Financial Planning",
    "prompt": "Create a comprehensive financial planning guide for divorce including asset division, income changes, expense restructuring, and rebuilding financial independence for:"
  },
  {
    "id": 420,
    "category": "finance",
    "title": "Career Change Financial Plan",
    "prompt": "Create a financial plan for a career change including runway calculation, expense reduction, income bridge strategy, benefit gaps, and new income ramp-up for:"
  },
  {
    "id": 421,
    "category": "finance",
    "title": "Charitable Giving Strategy",
    "prompt": "Design a strategic charitable giving plan with cause selection, giving vehicles, tax optimization, impact measurement, and legacy planning for:"
  },
  {
    "id": 422,
    "category": "finance",
    "title": "Financial Independence for Couples",
    "prompt": "Design a joint financial independence strategy for couples with shared goals, money communication, account structure, investment strategy, and conflict resolution for:"
  },
  {
    "id": 423,
    "category": "finance",
    "title": "Social Security Optimization",
    "prompt": "Design a Social Security claiming strategy analyzing break-even points, spousal benefits, survivor benefits, and tax implications for:"
  },
  {
    "id": 424,
    "category": "finance",
    "title": "HSA Optimization",
    "prompt": "Design a complete HSA optimization strategy as the ultimate triple tax-advantaged account for healthcare costs and retirement savings for:"
  },
  {
    "id": 425,
    "category": "finance",
    "title": "Backdoor Roth IRA",
    "prompt": "Explain and design a backdoor Roth IRA strategy including pro-rata rule considerations, conversion timing, tax implications, and annual execution for:"
  },
  {
    "id": 426,
    "category": "finance",
    "title": "Dollar Cost Averaging",
    "prompt": "Design a systematic dollar cost averaging program with investment amounts, frequency, rebalancing triggers, and psychological benefits for:"
  },
  {
    "id": 427,
    "category": "finance",
    "title": "Alternative Investments",
    "prompt": "Evaluate alternative investments (real estate, private equity, commodities, art) for portfolio diversification with allocation strategy and risk assessment for:"
  },
  {
    "id": 428,
    "category": "finance",
    "title": "Financial Independence Early Retirement",
    "prompt": "Design a complete FIRE strategy with FIRE number calculation, savings rate, investment approach, sequence of returns risk, and healthcare strategy for:"
  },
  {
    "id": 429,
    "category": "finance",
    "title": "Income Investing",
    "prompt": "Design an income-focused investment strategy with dividend stocks, REITs, bonds, and alternative income sources for generating reliable cash flow for:"
  },
  {
    "id": 430,
    "category": "finance",
    "title": "Value Investing",
    "prompt": "Design a value investing process with screening criteria, fundamental analysis, intrinsic value calculation, margin of safety, and portfolio management for:"
  },
  {
    "id": 431,
    "category": "finance",
    "title": "Growth Investing",
    "prompt": "Design a growth investing strategy with sector analysis, company evaluation, position sizing, entry/exit criteria, and portfolio construction for:"
  },
  {
    "id": 432,
    "category": "finance",
    "title": "Index Fund Strategy",
    "prompt": "Design an optimal index fund portfolio strategy with fund selection, asset allocation, rebalancing approach, tax-loss harvesting, and contribution strategy for:"
  },
  {
    "id": 433,
    "category": "finance",
    "title": "International Investing",
    "prompt": "Design an international investment strategy with geographic allocation, developed vs emerging markets, currency risk management, and vehicle selection for:"
  },
  {
    "id": 434,
    "category": "finance",
    "title": "Startup Investment",
    "prompt": "Design a startup investment strategy for angel investing with deal flow, due diligence process, portfolio construction, follow-on strategy, and exit planning for:"
  },
  {
    "id": 435,
    "category": "finance",
    "title": "Small Business Taxes",
    "prompt": "Design a comprehensive small business tax optimization strategy covering entity structure, deductions, retirement plans, estimated taxes, and year-end planning for:"
  },
  {
    "id": 436,
    "category": "finance",
    "title": "Real Estate vs Stocks",
    "prompt": "Analyze the real estate vs stock market investment decision with complete framework covering returns, leverage, liquidity, taxes, time requirements, and personal factors for:"
  },
  {
    "id": 437,
    "category": "finance",
    "title": "Financial Advisor Selection",
    "prompt": "Design a complete financial advisor evaluation framework with fee analysis, fiduciary standard, credentials verification, service model, and performance assessment for:"
  },
  {
    "id": 438,
    "category": "finance",
    "title": "Mortgage Optimization",
    "prompt": "Design a mortgage optimization strategy covering loan selection, points analysis, refinancing triggers, extra payment strategy, and overall home financing plan for:"
  },
  {
    "id": 439,
    "category": "finance",
    "title": "Financial Independence for Medical Professionals",
    "prompt": "Design a specialized financial independence plan for high-earning medical professionals addressing student loans, delayed start, high income strategies, and burnout planning for:"
  },
  {
    "id": 440,
    "category": "finance",
    "title": "Sequence of Returns Risk",
    "prompt": "Design a retirement portfolio strategy to manage sequence of returns risk with bucket strategy, dynamic withdrawal, asset allocation, and stress testing for:"
  },
  {
    "id": 441,
    "category": "design",
    "title": "Brand Identity System",
    "prompt": "Design a complete brand identity system with logo concept, color palette psychology, typography pairing, visual language, iconography style, and usage guidelines for:"
  },
  {
    "id": 442,
    "category": "design",
    "title": "UI Design System",
    "prompt": "Create a comprehensive UI design system with color tokens, typography scale, spacing system, component library, motion principles, and accessibility standards for:"
  },
  {
    "id": 443,
    "category": "design",
    "title": "UX Research Plan",
    "prompt": "Design a comprehensive UX research plan with research questions, methodology selection, participant recruitment, research instruments, analysis process, and reporting format for:"
  },
  {
    "id": 444,
    "category": "design",
    "title": "User Persona Development",
    "prompt": "Create detailed user personas with demographics, psychographics, goals, pain points, behaviors, technology use, and design implications based on research for:"
  },
  {
    "id": 445,
    "category": "design",
    "title": "Information Architecture",
    "prompt": "Design a complete information architecture with sitemap, navigation structure, content taxonomy, search strategy, and wayfinding system for:"
  },
  {
    "id": 446,
    "category": "design",
    "title": "Design Sprint Facilitation",
    "prompt": "Design a complete 5-day design sprint with daily activities, exercises, decision-making protocols, prototype specifications, and testing script for:"
  },
  {
    "id": 447,
    "category": "design",
    "title": "Accessibility Audit",
    "prompt": "Conduct a comprehensive accessibility audit covering WCAG 2.1 AA standards, color contrast, keyboard navigation, screen reader compatibility, and remediation plan for:"
  },
  {
    "id": 448,
    "category": "design",
    "title": "Mobile App UX",
    "prompt": "Design a complete mobile app user experience with user flows, wireframe descriptions, interaction patterns, gesture design, and usability principles for:"
  },
  {
    "id": 449,
    "category": "design",
    "title": "E-commerce UX",
    "prompt": "Design an optimal e-commerce user experience with product discovery, filtering, product pages, cart, checkout, and post-purchase experience for:"
  },
  {
    "id": 450,
    "category": "design",
    "title": "Dashboard Design",
    "prompt": "Design a data dashboard with information hierarchy, visualization selection, interaction patterns, responsive behavior, and performance optimization for:"
  },
  {
    "id": 451,
    "category": "design",
    "title": "Color Theory Application",
    "prompt": "Apply advanced color theory to create a sophisticated color system with primary, secondary, semantic, neutral palettes, dark mode variants, and accessibility compliance for:"
  },
  {
    "id": 452,
    "category": "design",
    "title": "Typography System",
    "prompt": "Design a comprehensive typography system with typeface selection rationale, scale, weight usage, line-height, letter-spacing, and responsive behavior for:"
  },
  {
    "id": 453,
    "category": "design",
    "title": "Illustration Style Guide",
    "prompt": "Create an illustration style guide with conceptual direction, line quality, color usage, composition principles, character design, and production specifications for:"
  },
  {
    "id": 454,
    "category": "design",
    "title": "Icon Design System",
    "prompt": "Design an icon system with visual style, grid system, construction rules, naming conventions, export specifications, and usage guidelines for:"
  },
  {
    "id": 455,
    "category": "design",
    "title": "Motion Design Principles",
    "prompt": "Create motion design principles with duration guidelines, easing functions, animation patterns, loading states, transitions, and performance considerations for:"
  },
  {
    "id": 456,
    "category": "design",
    "title": "Print Design System",
    "prompt": "Design a print design system with grid structure, typography, color usage, photography style, layout patterns, and production specifications for:"
  },
  {
    "id": 457,
    "category": "design",
    "title": "Packaging Design",
    "prompt": "Design a product packaging concept with structural considerations, visual hierarchy, material suggestions, printing techniques, and shelf impact for:"
  },
  {
    "id": 458,
    "category": "design",
    "title": "Presentation Design",
    "prompt": "Design a presentation template system with slide types, layout grid, typography, data visualization, imagery guidelines, and speaking notes format for:"
  },
  {
    "id": 459,
    "category": "design",
    "title": "Design Portfolio",
    "prompt": "Design a compelling design portfolio structure with case study format, project selection criteria, narrative approach, and online/offline presentation for:"
  },
  {
    "id": 460,
    "category": "design",
    "title": "User Testing Protocol",
    "prompt": "Design a comprehensive user testing protocol with task creation, participant screening, moderation guide, observation methods, and synthesis process for:"
  },
  {
    "id": 461,
    "category": "design",
    "title": "Responsive Design System",
    "prompt": "Design a responsive design system with breakpoints, fluid typography, flexible components, image strategy, and cross-device testing approach for:"
  },
  {
    "id": 462,
    "category": "design",
    "title": "Dark Mode Design",
    "prompt": "Design a complete dark mode experience with color inversion principles, contrast ratios, elevation system, imagery adaptation, and user preference handling for:"
  },
  {
    "id": 463,
    "category": "design",
    "title": "Onboarding Experience",
    "prompt": "Design a comprehensive product onboarding experience with empty states, progressive disclosure, tooltip tours, success milestones, and activation optimization for:"
  },
  {
    "id": 464,
    "category": "design",
    "title": "Error State Design",
    "prompt": "Design a comprehensive error state system with error types, messaging hierarchy, recovery actions, prevention strategies, and accessibility for:"
  },
  {
    "id": 465,
    "category": "design",
    "title": "Design Critique Framework",
    "prompt": "Create a structured design critique framework with evaluation criteria, feedback protocols, annotation methods, and constructive response guidelines for:"
  },
  {
    "id": 466,
    "category": "design",
    "title": "Creative Brief",
    "prompt": "Write a comprehensive creative brief with background, objectives, target audience, key message, tone, deliverables, constraints, and success metrics for:"
  },
  {
    "id": 467,
    "category": "design",
    "title": "Visual Identity Audit",
    "prompt": "Conduct a visual identity audit with competitive analysis, consistency assessment, brand alignment evaluation, and modernization recommendations for:"
  },
  {
    "id": 468,
    "category": "design",
    "title": "Design Handoff",
    "prompt": "Design a complete design handoff process with component documentation, spacing annotations, interaction specifications, asset export, and developer collaboration for:"
  },
  {
    "id": 469,
    "category": "design",
    "title": "Wayfinding System",
    "prompt": "Design a comprehensive wayfinding system for a physical or digital space with signage hierarchy, visual language, placement strategy, and accessibility for:"
  },
  {
    "id": 470,
    "category": "design",
    "title": "Service Design Blueprint",
    "prompt": "Create a service design blueprint with customer journey, frontstage actions, backstage actions, support processes, and pain point identification for:"
  },
  {
    "id": 471,
    "category": "design",
    "title": "Environmental Graphic Design",
    "prompt": "Design an environmental graphic design system for a physical space with concept, typography, wayfinding, murals, and installation guidelines for:"
  },
  {
    "id": 472,
    "category": "design",
    "title": "Design System Documentation",
    "prompt": "Create comprehensive design system documentation with component usage, do/don't examples, accessibility notes, code snippets, and contribution guidelines for:"
  },
  {
    "id": 473,
    "category": "design",
    "title": "Prototype Specification",
    "prompt": "Write a detailed prototype specification with interaction flows, state definitions, animation specs, edge cases, and handoff annotations for:"
  },
  {
    "id": 474,
    "category": "design",
    "title": "Design Strategy",
    "prompt": "Develop a design strategy with maturity assessment, vision, capability building, process improvement, and measuring design impact for:"
  },
  {
    "id": 475,
    "category": "design",
    "title": "Cultural Design Adaptation",
    "prompt": "Design a framework for adapting visual communication across cultures with color meanings, iconography, typography, layout direction, and imagery for:"
  },
  {
    "id": 476,
    "category": "design",
    "title": "Data Visualization Guide",
    "prompt": "Create a data visualization guide with chart type selection, color encoding, labeling standards, interactivity patterns, and storytelling principles for:"
  },
  {
    "id": 477,
    "category": "design",
    "title": "Voice UI Design",
    "prompt": "Design a voice user interface with conversation flows, error handling, disambiguation, personality, and multimodal interaction for:"
  },
  {
    "id": 478,
    "category": "design",
    "title": "AR/VR Experience Design",
    "prompt": "Design an augmented or virtual reality experience with spatial UI principles, depth usage, comfort considerations, interaction methods, and immersion design for:"
  },
  {
    "id": 479,
    "category": "design",
    "title": "Design Ethics Framework",
    "prompt": "Create a design ethics framework with value alignment, bias identification, inclusive design principles, environmental impact, and accountability processes for:"
  },
  {
    "id": 480,
    "category": "design",
    "title": "Retail Experience Design",
    "prompt": "Design a complete retail experience with store layout, visual merchandising, digital integration, staff interaction design, and measurement for:"
  },
  {
    "id": 481,
    "category": "design",
    "title": "Healthcare UX Design",
    "prompt": "Design a healthcare user experience prioritizing clarity, accessibility, error prevention, trust building, and emotional sensitivity for:"
  },
  {
    "id": 482,
    "category": "design",
    "title": "Children's Product Design",
    "prompt": "Design a children's product experience with age-appropriateness, safety considerations, engagement mechanics, parental controls, and learning integration for:"
  },
  {
    "id": 483,
    "category": "design",
    "title": "Design Leadership",
    "prompt": "Develop a design leadership strategy with team structure, hiring approach, culture building, process development, and measuring design's business impact for:"
  },
  {
    "id": 484,
    "category": "design",
    "title": "Micro-interactions Design",
    "prompt": "Design a comprehensive micro-interaction system with trigger-feedback loops, animation principles, haptic patterns, and system personality for:"
  },
  {
    "id": 485,
    "category": "design",
    "title": "Empty State Design",
    "prompt": "Design a comprehensive empty state system that guides users, sets expectations, encourages action, and maintains brand personality for:"
  },
  {
    "id": 486,
    "category": "design",
    "title": "Design Token System",
    "prompt": "Create a design token system with naming conventions, value organization, theming support, platform exports, and documentation for:"
  },
  {
    "id": 487,
    "category": "design",
    "title": "Creative Direction",
    "prompt": "Develop a creative direction document with visual concept, mood board description, photography art direction, illustration approach, and overall aesthetic for:"
  },
  {
    "id": 488,
    "category": "design",
    "title": "Form Design Optimization",
    "prompt": "Design an optimized form experience with field order, input types, validation timing, error recovery, progress indication, and completion optimization for:"
  },
  {
    "id": 489,
    "category": "design",
    "title": "Navigation Design",
    "prompt": "Design a comprehensive navigation system for complex content with primary, secondary, contextual, and utility navigation, search, and breadcrumbs for:"
  },
  {
    "id": 490,
    "category": "career",
    "title": "Career Change Roadmap",
    "prompt": "Create a comprehensive career change roadmap with transferable skills analysis, skill gaps, education plan, network building, portfolio development, and job search strategy for someone transitioning from:"
  },
  {
    "id": 491,
    "category": "career",
    "title": "LinkedIn Profile Optimization",
    "prompt": "Write a complete LinkedIn profile optimization with headline, about section, experience bullets, skills, recommendations request, and content strategy for:"
  },
  {
    "id": 492,
    "category": "career",
    "title": "Salary Negotiation Script",
    "prompt": "Write a detailed salary negotiation preparation guide with research methodology, opening ask, justification points, counter-offer response, and alternative compensation for:"
  },
  {
    "id": 493,
    "category": "career",
    "title": "Interview Preparation",
    "prompt": "Create a comprehensive interview preparation guide with company research framework, STAR story bank, difficult question responses, questions to ask, and follow-up strategy for:"
  },
  {
    "id": 494,
    "category": "career",
    "title": "Personal Brand Strategy",
    "prompt": "Develop a complete personal brand strategy with unique positioning, content themes, platform selection, thought leadership plan, and visibility building for:"
  },
  {
    "id": 495,
    "category": "career",
    "title": "Resume Optimization",
    "prompt": "Write a highly optimized resume with compelling summary, achievement-focused bullets with metrics, ATS optimization, and formatting for the following role:"
  },
  {
    "id": 496,
    "category": "career",
    "title": "Career Development Plan",
    "prompt": "Design a comprehensive 3-year career development plan with role progression, skill development, experience building, relationship cultivation, and milestone tracking for:"
  },
  {
    "id": 497,
    "category": "career",
    "title": "Executive Presence",
    "prompt": "Develop an executive presence improvement plan covering communication style, strategic thinking demonstration, relationship building, and leadership visibility for:"
  },
  {
    "id": 498,
    "category": "career",
    "title": "Networking Strategy",
    "prompt": "Design a systematic professional networking strategy with relationship mapping, outreach templates, value-giving approach, follow-up system, and event strategy for:"
  },
  {
    "id": 499,
    "category": "career",
    "title": "Portfolio Building",
    "prompt": "Design a comprehensive professional portfolio strategy with project selection, case study structure, online presence, presentation format, and ongoing maintenance for:"
  },
  {
    "id": 500,
    "category": "career",
    "title": "Leadership Development",
    "prompt": "Design a comprehensive leadership development plan covering self-awareness, communication, strategic thinking, team building, and organizational influence for:"
  },
  {
    "id": 501,
    "category": "career",
    "title": "Mentorship Strategy",
    "prompt": "Design a strategic mentorship program as both mentee and mentor with goal setting, relationship building, meeting structure, and value exchange for:"
  },
  {
    "id": 502,
    "category": "career",
    "title": "Workplace Conflict Resolution",
    "prompt": "Design a professional conflict resolution approach with situation assessment, conversation preparation, dialogue techniques, escalation criteria, and relationship repair for:"
  },
  {
    "id": 503,
    "category": "career",
    "title": "Performance Improvement",
    "prompt": "Design a performance improvement strategy with self-assessment, goal setting, skill development, visibility improvement, and progress demonstration for:"
  },
  {
    "id": 504,
    "category": "career",
    "title": "Job Search Strategy",
    "prompt": "Design a comprehensive job search strategy with target company list, outreach approach, application optimization, interview pipeline management, and offer evaluation for:"
  },
  {
    "id": 505,
    "category": "career",
    "title": "Freelance Business Launch",
    "prompt": "Design a complete freelance business launch plan with niche selection, service packaging, pricing strategy, client acquisition, and operations setup for:"
  },
  {
    "id": 506,
    "category": "career",
    "title": "Promotion Strategy",
    "prompt": "Design a systematic promotion pursuit strategy with visibility building, skill demonstration, advocate cultivation, timing, and negotiation preparation for:"
  },
  {
    "id": 507,
    "category": "career",
    "title": "Career Pivot Strategy",
    "prompt": "Design a strategic career pivot plan with transferable assets inventory, target role analysis, bridge building, credibility establishment, and transition timeline for:"
  },
  {
    "id": 508,
    "category": "career",
    "title": "Work From Home Productivity",
    "prompt": "Design a complete remote work professional strategy covering home office setup, communication excellence, visibility maintenance, and career advancement while remote for:"
  },
  {
    "id": 509,
    "category": "career",
    "title": "Difficult Boss Management",
    "prompt": "Design a strategy for managing up with a difficult boss including communication adaptation, expectation alignment, trust building, and escalation criteria for:"
  },
  {
    "id": 510,
    "category": "career",
    "title": "Team Leadership",
    "prompt": "Design a first-time manager success plan covering team assessment, quick wins, relationship building, performance management, and leadership style development for:"
  },
  {
    "id": 511,
    "category": "career",
    "title": "Career Recovery",
    "prompt": "Design a career recovery strategy after setback (layoff, poor review, failed project) with narrative reframing, skill gap addressing, and accelerated rebuilding for:"
  },
  {
    "id": 512,
    "category": "career",
    "title": "Industry Expertise Building",
    "prompt": "Design a systematic industry expertise building program with learning resources, community engagement, thought leadership, speaking, and recognition strategy for:"
  },
  {
    "id": 513,
    "category": "career",
    "title": "Technical Interview Preparation",
    "prompt": "Design a comprehensive technical interview preparation plan with concept review, problem-solving practice, system design, behavioral questions, and mock interview schedule for:"
  },
  {
    "id": 514,
    "category": "career",
    "title": "Career Sponsor Strategy",
    "prompt": "Design a strategy for finding and working with sponsors (not just mentors) who will advocate for your advancement with identification, cultivation, and leveraging for:"
  },
  {
    "id": 515,
    "category": "career",
    "title": "Side Business to Main Career",
    "prompt": "Design a transition plan from employed professional to full-time entrepreneur with financial runway, client building, legal setup, and risk management for:"
  },
  {
    "id": 516,
    "category": "career",
    "title": "Academic to Industry Transition",
    "prompt": "Design a career transition plan from academia to industry with skills translation, network building, portfolio creation, and interview preparation for:"
  },
  {
    "id": 517,
    "category": "career",
    "title": "International Career",
    "prompt": "Design an international career strategy with country selection, credential recognition, language preparation, cultural adaptation, visa navigation, and network building for:"
  },
  {
    "id": 518,
    "category": "career",
    "title": "Career Comeback",
    "prompt": "Design a career comeback strategy for someone returning after extended absence (parental leave, illness, caregiving) with skills update, narrative, and market reentry for:"
  },
  {
    "id": 519,
    "category": "career",
    "title": "Entrepreneurial Transition",
    "prompt": "Design a transition plan from corporate employee to entrepreneur including mindset shifts, financial preparation, network leverage, and first 90 days as founder for:"
  },
  {
    "id": 520,
    "category": "career",
    "title": "C-Suite Preparation",
    "prompt": "Design a pathway to C-suite leadership with capability building, visibility strategy, board relationships, P&L experience, and executive coaching for:"
  },
  {
    "id": 521,
    "category": "career",
    "title": "Career Diversification",
    "prompt": "Design a career diversification strategy with portfolio career development, multiple income streams, skills cross-pollination, and risk management for:"
  },
  {
    "id": 522,
    "category": "career",
    "title": "Negotiating Benefits",
    "prompt": "Design a comprehensive benefits negotiation strategy covering beyond salary: equity, PTO, remote work, development budget, signing bonus, and review timing for:"
  },
  {
    "id": 523,
    "category": "career",
    "title": "Career Narrative",
    "prompt": "Craft a compelling career narrative that connects disparate experiences into a coherent story of growth, expertise, and unique value for:"
  },
  {
    "id": 524,
    "category": "career",
    "title": "Professional Development Budget",
    "prompt": "Design a strategy for maximizing a professional development budget with highest-ROI investments in courses, conferences, coaching, and experiences for:"
  },
  {
    "id": 525,
    "category": "career",
    "title": "Building Thought Leadership",
    "prompt": "Design a systematic thought leadership building program with content strategy, publishing plan, speaking circuit, podcast appearances, and community building for:"
  },
  {
    "id": 526,
    "category": "career",
    "title": "Career Satisfaction Assessment",
    "prompt": "Design a comprehensive career satisfaction assessment with multiple dimensions, diagnostic questions, root cause analysis, and action planning for:"
  },
  {
    "id": 527,
    "category": "career",
    "title": "Skills Gap Analysis",
    "prompt": "Conduct a thorough skills gap analysis with current state assessment, target role requirements, priority gaps, development resources, and acquisition timeline for:"
  },
  {
    "id": 528,
    "category": "career",
    "title": "Cross-Functional Leadership",
    "prompt": "Design a strategy for building cross-functional influence and leadership without formal authority through coalition building, shared goals, and value creation for:"
  },
  {
    "id": 529,
    "category": "career",
    "title": "Entrepreneur to Employee Transition",
    "prompt": "Design a transition plan for entrepreneurs returning to corporate employment with narrative positioning, expectation management, and culture adaptation for:"
  },
  {
    "id": 530,
    "category": "career",
    "title": "Career Coaching Practice",
    "prompt": "Design a career coaching practice business plan with niche selection, methodology development, client acquisition, program structure, and pricing for:"
  },
  {
    "id": 531,
    "category": "career",
    "title": "Workforce Reentry",
    "prompt": "Design a comprehensive workforce reentry strategy for someone returning after 5+ years away with skills update, narrative, network rebuild, and search strategy for:"
  },
  {
    "id": 532,
    "category": "career",
    "title": "Innovation Leadership",
    "prompt": "Design an innovation leadership development plan for corporate innovators covering idea generation, coalition building, risk management, and organizational navigation for:"
  },
  {
    "id": 533,
    "category": "career",
    "title": "Purpose-Driven Career",
    "prompt": "Design a purpose-driven career development strategy with values clarification, purpose articulation, opportunity assessment, and meaningful contribution building for:"
  },
  {
    "id": 534,
    "category": "career",
    "title": "Board Director Preparation",
    "prompt": "Design a preparation pathway for aspiring board directors with skill building, network development, governance education, and board search strategy for:"
  },
  {
    "id": 535,
    "category": "career",
    "title": "Career Transition at 50+",
    "prompt": "Design a career transition strategy specifically for professionals over 50 addressing age bias, digital skills, network leverage, and positioning for:"
  },
  {
    "id": 536,
    "category": "career",
    "title": "Technical to Management",
    "prompt": "Design a transition plan from individual contributor to people manager covering mindset shift, new competencies, relationship rebuilding, and early wins for:"
  },
  {
    "id": 537,
    "category": "career",
    "title": "Global Leadership",
    "prompt": "Design a global leadership development plan with cross-cultural competence, international experience, global network building, and global business acumen for:"
  },
  {
    "id": 538,
    "category": "science",
    "title": "Research Hypothesis",
    "prompt": "Formulate a precise, testable research hypothesis with null hypothesis, alternative hypothesis, variables, measurement methods, and statistical analysis plan for:"
  },
  {
    "id": 539,
    "category": "science",
    "title": "Literature Review",
    "prompt": "Write a systematic literature review with search strategy, inclusion criteria, synthesis methodology, gap identification, and future research directions for:"
  },
  {
    "id": 540,
    "category": "science",
    "title": "Experiment Design",
    "prompt": "Design a rigorous scientific experiment with control groups, variables, sample size calculation, methodology, statistical analysis, and ethical considerations for:"
  },
  {
    "id": 541,
    "category": "science",
    "title": "Data Analysis Plan",
    "prompt": "Create a comprehensive data analysis plan with descriptive statistics, inferential tests, visualization strategy, and interpretation framework for:"
  },
  {
    "id": 542,
    "category": "science",
    "title": "Science Communication",
    "prompt": "Write a science communication piece that translates complex research findings into engaging, accurate, and accessible content for a general audience about:"
  },
  {
    "id": 543,
    "category": "science",
    "title": "Grant Writing",
    "prompt": "Write a compelling research grant proposal with specific aims, background, innovation, approach, significance, and investigator qualifications for:"
  },
  {
    "id": 544,
    "category": "science",
    "title": "Scientific Poster",
    "prompt": "Design a scientific poster layout with key findings, methodology summary, visual data presentation, and compelling takeaway message for:"
  },
  {
    "id": 545,
    "category": "science",
    "title": "Peer Review",
    "prompt": "Write a constructive peer review with major concerns, minor concerns, specific suggestions, strengths acknowledgment, and recommendation for:"
  },
  {
    "id": 546,
    "category": "science",
    "title": "Meta-Analysis",
    "prompt": "Design a meta-analysis protocol with PICO framework, search strategy, quality assessment, statistical synthesis, and heterogeneity analysis for:"
  },
  {
    "id": 547,
    "category": "science",
    "title": "Science Policy Brief",
    "prompt": "Write a science policy brief connecting research evidence to policy recommendations with executive summary, evidence synthesis, and specific recommendations for:"
  },
  {
    "id": 548,
    "category": "science",
    "title": "Research Ethics",
    "prompt": "Design a research ethics framework covering informed consent, privacy protection, conflict of interest, data integrity, and participant safety for:"
  },
  {
    "id": 549,
    "category": "science",
    "title": "Citizen Science Project",
    "prompt": "Design a citizen science project with research goals, volunteer tasks, data quality control, engagement strategy, and impact communication for:"
  },
  {
    "id": 550,
    "category": "science",
    "title": "Science Curriculum",
    "prompt": "Design a science curriculum that builds conceptual understanding, scientific practices, and cross-cutting concepts using phenomena-based learning for:"
  },
  {
    "id": 551,
    "category": "science",
    "title": "Laboratory Protocol",
    "prompt": "Write a detailed laboratory protocol with safety precautions, materials list, step-by-step procedure, quality controls, and troubleshooting guide for:"
  },
  {
    "id": 552,
    "category": "science",
    "title": "Scientific Presentation",
    "prompt": "Design a compelling scientific presentation with narrative structure, data visualization, methods clarity, limitations honesty, and implications for:"
  },
  {
    "id": 553,
    "category": "science",
    "title": "Technology Assessment",
    "prompt": "Conduct a technology assessment covering current capabilities, limitations, societal implications, ethical concerns, and future development trajectory for:"
  },
  {
    "id": 554,
    "category": "science",
    "title": "Climate Science Communication",
    "prompt": "Write compelling climate science communication that is accurate, non-alarmist, action-oriented, and addresses common misconceptions about:"
  },
  {
    "id": 555,
    "category": "science",
    "title": "Medical Research Translation",
    "prompt": "Translate complex medical research into patient-friendly information covering what it means, what to do, limitations, and next steps for:"
  },
  {
    "id": 556,
    "category": "science",
    "title": "Science Fiction Plausibility",
    "prompt": "Analyze the scientific plausibility of the following science fiction concept and design a version that maximizes scientific accuracy while maintaining narrative appeal:"
  },
  {
    "id": 557,
    "category": "science",
    "title": "Research Collaboration",
    "prompt": "Design a research collaboration framework with role clarity, data sharing protocols, publication agreements, conflict resolution, and intellectual property for:"
  },
  {
    "id": 558,
    "category": "science",
    "title": "Science Journalism",
    "prompt": "Write a science journalism piece that accurately represents research findings, provides context, includes expert voices, and avoids sensationalism about:"
  },
  {
    "id": 559,
    "category": "science",
    "title": "Replication Study",
    "prompt": "Design a high-quality replication study with faithful methodology reproduction, appropriate sample, pre-registration, and transparent reporting for:"
  },
  {
    "id": 560,
    "category": "science",
    "title": "Systematic Review Protocol",
    "prompt": "Write a systematic review protocol with PRISMA guidelines, search strategy, data extraction form, risk of bias assessment, and synthesis approach for:"
  },
  {
    "id": 561,
    "category": "science",
    "title": "Science Museum Exhibit",
    "prompt": "Design an interactive science museum exhibit with learning objectives, hands-on activities, information hierarchy, accessibility, and evaluation plan for:"
  },
  {
    "id": 562,
    "category": "science",
    "title": "Scientific Writing",
    "prompt": "Write a complete scientific paper section (methods/results/discussion) following journal standards with appropriate hedging, citation style, and statistical reporting for:"
  },
  {
    "id": 563,
    "category": "technology",
    "title": "AI Implementation Strategy",
    "prompt": "Develop a comprehensive AI implementation strategy with use case prioritization, build/buy/partner analysis, data requirements, ethical framework, and change management for:"
  },
  {
    "id": 564,
    "category": "technology",
    "title": "Cloud Migration Plan",
    "prompt": "Create a complete cloud migration plan with workload assessment, migration approach, timeline, cost analysis, risk mitigation, and post-migration optimization for:"
  },
  {
    "id": 565,
    "category": "technology",
    "title": "Cybersecurity Strategy",
    "prompt": "Design a comprehensive cybersecurity strategy with threat modeling, security controls, incident response, employee training, and compliance framework for:"
  },
  {
    "id": 566,
    "category": "technology",
    "title": "Digital Transformation",
    "prompt": "Develop a digital transformation strategy with technology assessment, process redesign, capability building, change management, and value measurement for:"
  },
  {
    "id": 567,
    "category": "technology",
    "title": "Data Strategy",
    "prompt": "Create a comprehensive data strategy with data governance, architecture, quality management, analytics capabilities, and privacy compliance for:"
  },
  {
    "id": 568,
    "category": "technology",
    "title": "Technology Roadmap",
    "prompt": "Design a 3-year technology roadmap with current state assessment, target architecture, initiative prioritization, resource requirements, and success metrics for:"
  },
  {
    "id": 569,
    "category": "technology",
    "title": "Software Evaluation",
    "prompt": "Design a comprehensive software evaluation framework with requirements definition, vendor assessment, proof of concept, TCO analysis, and selection criteria for:"
  },
  {
    "id": 570,
    "category": "technology",
    "title": "IT Governance",
    "prompt": "Design an IT governance framework with decision rights, portfolio management, project governance, risk management, and performance measurement for:"
  },
  {
    "id": 571,
    "category": "technology",
    "title": "API Strategy",
    "prompt": "Develop a comprehensive API strategy with design standards, security model, developer experience, versioning, monetization, and ecosystem building for:"
  },
  {
    "id": 572,
    "category": "technology",
    "title": "Innovation Lab",
    "prompt": "Design an innovation lab concept with focus areas, operating model, talent strategy, partnership approach, and success measurement for:"
  },
  {
    "id": 573,
    "category": "technology",
    "title": "Technology Due Diligence",
    "prompt": "Design a technology due diligence framework for M&A covering architecture, code quality, technical debt, team assessment, and integration complexity for:"
  },
  {
    "id": 574,
    "category": "technology",
    "title": "Platform Strategy",
    "prompt": "Develop a platform strategy with network effect design, participant incentives, governance model, monetization, and ecosystem development for:"
  },
  {
    "id": 575,
    "category": "technology",
    "title": "IoT Architecture",
    "prompt": "Design an IoT solution architecture with device selection, connectivity, data ingestion, processing, storage, analytics, and security for:"
  },
  {
    "id": 576,
    "category": "technology",
    "title": "Blockchain Use Case",
    "prompt": "Evaluate a blockchain implementation use case with technology fit analysis, architecture design, governance model, and implementation roadmap for:"
  },
  {
    "id": 577,
    "category": "technology",
    "title": "Quantum Computing Preparation",
    "prompt": "Develop a quantum computing readiness strategy with use case identification, team capability building, classical migration, and timeline for:"
  },
  {
    "id": 578,
    "category": "technology",
    "title": "Edge Computing Strategy",
    "prompt": "Design an edge computing strategy with workload assessment, infrastructure design, data management, security, and operational model for:"
  },
  {
    "id": 579,
    "category": "technology",
    "title": "5G Implementation",
    "prompt": "Design a 5G technology strategy with use case prioritization, network slicing, application development, security, and business value realization for:"
  },
  {
    "id": 580,
    "category": "technology",
    "title": "Digital Twin",
    "prompt": "Design a digital twin implementation with physical asset mapping, data collection, simulation modeling, insights generation, and operational integration for:"
  },
  {
    "id": 581,
    "category": "technology",
    "title": "Augmented Reality Enterprise",
    "prompt": "Design an enterprise AR strategy with use case identification, hardware selection, content development, training, and ROI measurement for:"
  },
  {
    "id": 582,
    "category": "technology",
    "title": "DevSecOps Implementation",
    "prompt": "Design a DevSecOps implementation with security integration points, toolchain, automation, training, and metrics for measuring security quality for:"
  },
  {
    "id": 583,
    "category": "technology",
    "title": "Open Source Strategy",
    "prompt": "Develop an enterprise open source strategy with consumption governance, contribution approach, community engagement, and risk management for:"
  },
  {
    "id": 584,
    "category": "technology",
    "title": "Data Privacy Architecture",
    "prompt": "Design a privacy-by-design architecture with data minimization, consent management, access controls, anonymization, and breach response for:"
  },
  {
    "id": 585,
    "category": "technology",
    "title": "Technology Skills Assessment",
    "prompt": "Design a technology skills assessment and development program with competency mapping, assessment tools, learning pathways, and certification for:"
  },
  {
    "id": 586,
    "category": "technology",
    "title": "Vendor Management",
    "prompt": "Design a technology vendor management program with selection criteria, contract negotiation, performance management, and relationship governance for:"
  },
  {
    "id": 587,
    "category": "technology",
    "title": "Disaster Recovery",
    "prompt": "Design a comprehensive disaster recovery plan with RTO/RPO objectives, backup strategy, failover procedures, testing schedule, and communication plan for:"
  },
  {
    "id": 588,
    "category": "psychology",
    "title": "Cognitive Behavioral Therapy",
    "prompt": "Explain CBT concepts and design a self-guided CBT program with thought records, behavioral experiments, cognitive restructuring, and maintenance plan for:"
  },
  {
    "id": 589,
    "category": "psychology",
    "title": "Behavior Change Design",
    "prompt": "Design a behavior change program using COM-B model, behavioral economics, habit formation, and motivation theories for:"
  },
  {
    "id": 590,
    "category": "psychology",
    "title": "Emotional Intelligence Development",
    "prompt": "Design an emotional intelligence development program covering self-awareness, self-regulation, motivation, empathy, and social skills for:"
  },
  {
    "id": 591,
    "category": "psychology",
    "title": "Positive Psychology Intervention",
    "prompt": "Design a positive psychology intervention program with strengths assessment, gratitude practice, flow cultivation, meaning building, and wellbeing measurement for:"
  },
  {
    "id": 592,
    "category": "psychology",
    "title": "Motivation System",
    "prompt": "Design a motivation system using self-determination theory, goal setting, intrinsic motivation, and progress tracking for:"
  },
  {
    "id": 593,
    "category": "psychology",
    "title": "Cognitive Biases",
    "prompt": "Identify the top 20 cognitive biases most relevant to the following decision context and design debiasing interventions for each:"
  },
  {
    "id": 594,
    "category": "psychology",
    "title": "Relationship Psychology",
    "prompt": "Design a relationship improvement program based on attachment theory, communication research, and relationship science for:"
  },
  {
    "id": 595,
    "category": "psychology",
    "title": "Leadership Psychology",
    "prompt": "Apply psychological principles to leadership development covering personality assessment, emotional regulation, influence, decision-making, and resilience for:"
  },
  {
    "id": 596,
    "category": "psychology",
    "title": "Consumer Psychology",
    "prompt": "Apply consumer psychology principles to improve customer experience, decision architecture, persuasion ethics, and loyalty for:"
  },
  {
    "id": 597,
    "category": "psychology",
    "title": "Trauma-Informed Approach",
    "prompt": "Design a trauma-informed approach for the following context covering safety, trustworthiness, choice, collaboration, and empowerment for:"
  },
  {
    "id": 598,
    "category": "psychology",
    "title": "Positive Habit Formation",
    "prompt": "Design a scientifically-grounded habit formation program using cue-routine-reward, implementation intentions, temptation bundling, and social accountability for:"
  },
  {
    "id": 599,
    "category": "psychology",
    "title": "Growth Mindset Cultivation",
    "prompt": "Design a growth mindset cultivation program with mindset diagnostics, challenge reframing, failure processing, and learning identity building for:"
  },
  {
    "id": 600,
    "category": "psychology",
    "title": "Psychological Safety",
    "prompt": "Design a psychological safety building program for teams with assessment, leader behaviors, team norms, speaking up structures, and measurement for:"
  },
  {
    "id": 601,
    "category": "psychology",
    "title": "Negotiation Psychology",
    "prompt": "Apply negotiation psychology principles including anchoring, loss aversion, reciprocity, and relationship building to optimize outcomes for:"
  },
  {
    "id": 602,
    "category": "psychology",
    "title": "Performance Psychology",
    "prompt": "Design a performance psychology program for high achievers covering pre-performance routines, focus techniques, adversity response, and peak performance for:"
  },
  {
    "id": 603,
    "category": "psychology",
    "title": "Social Influence",
    "prompt": "Apply principles of social influence (reciprocity, commitment, social proof, authority, liking, scarcity) ethically to:"
  },
  {
    "id": 604,
    "category": "psychology",
    "title": "Resilience Program",
    "prompt": "Design a psychological resilience program with adversity response training, cognitive flexibility, emotional regulation, social support, and meaning-making for:"
  },
  {
    "id": 605,
    "category": "psychology",
    "title": "Behavior Analysis",
    "prompt": "Conduct a behavioral analysis using ABC (Antecedent-Behavior-Consequence) framework with intervention design and progress monitoring for:"
  },
  {
    "id": 606,
    "category": "psychology",
    "title": "Persuasion Ethics",
    "prompt": "Design an ethical persuasion strategy that influences behavior while respecting autonomy, transparency, and long-term wellbeing for:"
  },
  {
    "id": 607,
    "category": "psychology",
    "title": "Well-being Assessment",
    "prompt": "Design a comprehensive well-being assessment covering hedonic and eudaimonic well-being, measurement tools, and intervention matching for:"
  },
  {
    "id": 608,
    "category": "psychology",
    "title": "Organizational Psychology",
    "prompt": "Apply organizational psychology to improve culture, engagement, performance management, leadership, and organizational change for:"
  },
  {
    "id": 609,
    "category": "psychology",
    "title": "Educational Psychology",
    "prompt": "Apply educational psychology principles to improve learning design, motivation, assessment, and learning environment for:"
  },
  {
    "id": 610,
    "category": "psychology",
    "title": "Sports Psychology",
    "prompt": "Design a sports psychology program covering mental toughness, focus, confidence, team cohesion, and competition preparation for:"
  },
  {
    "id": 611,
    "category": "psychology",
    "title": "Positive Parenting",
    "prompt": "Design a positive parenting program based on developmental psychology, attachment, autonomy support, and authoritative parenting research for:"
  },
  {
    "id": 612,
    "category": "psychology",
    "title": "Mindfulness-Based Stress Reduction",
    "prompt": "Design a structured MBSR program with formal practices, informal integration, inquiry process, and outcome measurement for:"
  },
  {
    "id": 613,
    "category": "travel",
    "title": "Dream Trip Planning",
    "prompt": "Create a comprehensive dream trip itinerary with day-by-day activities, accommodation recommendations, restaurant selections, transportation, budget breakdown, and local tips for:"
  },
  {
    "id": 614,
    "category": "travel",
    "title": "Budget Travel Strategy",
    "prompt": "Design a complete budget travel system with cost reduction strategies, accommodation options, food hacks, free activities, and money-saving transportation for:"
  },
  {
    "id": 615,
    "category": "travel",
    "title": "Solo Travel Safety",
    "prompt": "Design a comprehensive solo travel safety plan with pre-departure preparation, situational awareness, emergency protocols, communication check-ins, and risk mitigation for:"
  },
  {
    "id": 616,
    "category": "travel",
    "title": "Cultural Immersion",
    "prompt": "Design a cultural immersion travel experience with language learning, local community connections, authentic cuisine, cultural events, and responsible tourism for:"
  },
  {
    "id": 617,
    "category": "travel",
    "title": "Digital Nomad Setup",
    "prompt": "Design a complete digital nomad lifestyle setup with best destinations, accommodation options, workspace finding, internet reliability, tax considerations, and community for:"
  },
  {
    "id": 618,
    "category": "travel",
    "title": "Adventure Travel Planning",
    "prompt": "Design an adventure travel expedition with activity planning, physical preparation, gear list, safety protocols, guide selection, and emergency procedures for:"
  },
  {
    "id": 619,
    "category": "travel",
    "title": "Family Travel Planning",
    "prompt": "Design a family travel itinerary that works for all ages with child-friendly activities, flexible scheduling, rest time, budget management, and memory-making for:"
  },
  {
    "id": 620,
    "category": "travel",
    "title": "Sustainable Travel",
    "prompt": "Design a sustainable travel plan that minimizes environmental impact while maximizing experience through accommodation choice, transportation, activities, and offset for:"
  },
  {
    "id": 621,
    "category": "travel",
    "title": "Travel Photography",
    "prompt": "Design a travel photography strategy with shot list, equipment, lighting, storytelling, editing workflow, and sharing strategy for:"
  },
  {
    "id": 622,
    "category": "travel",
    "title": "Travel Journaling",
    "prompt": "Design a comprehensive travel journaling practice with prompts, documentation methods, artifact collection, and memory preservation for:"
  },
  {
    "id": 623,
    "category": "travel",
    "title": "Long-Term Travel",
    "prompt": "Design a long-term world travel plan with route optimization, visa strategy, health preparation, financial management, and work-life integration for:"
  },
  {
    "id": 624,
    "category": "travel",
    "title": "Travel Hacking",
    "prompt": "Design a travel hacking strategy with credit card optimization, airline miles, hotel points, status benefits, and award booking for maximizing value for:"
  },
  {
    "id": 625,
    "category": "travel",
    "title": "Medical Travel Preparation",
    "prompt": "Create a comprehensive travel health preparation plan with vaccinations, medications, insurance, emergency contacts, and destination-specific health risks for:"
  },
  {
    "id": 626,
    "category": "travel",
    "title": "Business Travel Optimization",
    "prompt": "Design a business travel optimization strategy with packing system, productivity maintenance, jet lag management, expense tracking, and points maximization for:"
  },
  {
    "id": 627,
    "category": "travel",
    "title": "Travel Writing",
    "prompt": "Write compelling travel content that captures sense of place, cultural nuance, practical information, and personal transformation for:"
  },
  {
    "id": 628,
    "category": "travel",
    "title": "Culinary Travel",
    "prompt": "Design a culinary travel experience with food research, market visits, cooking classes, restaurant selection, street food strategy, and food documentation for:"
  },
  {
    "id": 629,
    "category": "travel",
    "title": "Volunteer Travel",
    "prompt": "Design a meaningful volunteer travel experience with program vetting, skill matching, community impact, ethical considerations, and integration with personal goals for:"
  },
  {
    "id": 630,
    "category": "travel",
    "title": "Luxury Travel Planning",
    "prompt": "Design an ultra-luxury travel experience with exclusive accommodations, private guides, unique access, personalized experiences, and seamless logistics for:"
  },
  {
    "id": 631,
    "category": "travel",
    "title": "Travel Packing System",
    "prompt": "Design a comprehensive packing system for different travel types with capsule wardrobe, gear organization, weight optimization, and security for:"
  },
  {
    "id": 632,
    "category": "travel",
    "title": "Off-The-Beaten-Path",
    "prompt": "Design an off-the-beaten-path travel experience with alternative destinations, local connections, authentic experiences, and responsible discovery for:"
  },
  {
    "id": 633,
    "category": "travel",
    "title": "Retreat Planning",
    "prompt": "Design a wellness or creative retreat experience with location selection, daily schedule, facilitator selection, participant preparation, and integration support for:"
  },
  {
    "id": 634,
    "category": "travel",
    "title": "Road Trip Planning",
    "prompt": "Design an epic road trip with route optimization, scenic highlights, accommodation strategy, car preparation, activity planning, and food stops for:"
  },
  {
    "id": 635,
    "category": "travel",
    "title": "Travel on a Shoestring",
    "prompt": "Design an extreme budget travel plan for seeing maximum destinations on minimum daily budget with creative accommodation, food, and transportation strategies for:"
  },
  {
    "id": 636,
    "category": "travel",
    "title": "Expat Life Preparation",
    "prompt": "Design a comprehensive expatriate life preparation plan with destination research, visa requirements, housing, healthcare, schooling, community building, and adjustment for:"
  },
  {
    "id": 637,
    "category": "travel",
    "title": "Group Travel Coordination",
    "prompt": "Design a group travel coordination system with consensus building, role assignment, booking management, expense splitting, and conflict prevention for:"
  },
  {
    "id": 638,
    "category": "parenting",
    "title": "Child Development Plan",
    "prompt": "Design a holistic child development support plan aligned with developmental stages covering cognitive, social, emotional, physical, and language development for a child who is:"
  },
  {
    "id": 639,
    "category": "parenting",
    "title": "Family Communication",
    "prompt": "Design a family communication system that builds connection, resolves conflicts, ensures everyone feels heard, and creates lasting family culture for:"
  },
  {
    "id": 640,
    "category": "parenting",
    "title": "Screen Time Management",
    "prompt": "Design a thoughtful screen time management approach with boundaries, quality content selection, co-viewing, digital literacy, and balance with other activities for:"
  },
  {
    "id": 641,
    "category": "parenting",
    "title": "Homework Help Strategy",
    "prompt": "Design a homework support system that builds independence, maintains motivation, prevents battles, develops organizational skills, and supports academic success for:"
  },
  {
    "id": 642,
    "category": "parenting",
    "title": "Emotional Coaching",
    "prompt": "Design an emotional coaching approach for parents using Gottman's emotion coaching model with validation, problem-solving, and boundary setting for:"
  },
  {
    "id": 643,
    "category": "parenting",
    "title": "Sibling Relationship Building",
    "prompt": "Design strategies for building positive sibling relationships with conflict resolution skills, individual attention, shared experiences, and long-term bonding for:"
  },
  {
    "id": 644,
    "category": "parenting",
    "title": "Positive Discipline",
    "prompt": "Design a positive discipline system with logical consequences, natural consequences, problem-solving meetings, encouragement, and connection-before-correction for:"
  },
  {
    "id": 645,
    "category": "parenting",
    "title": "Raising Confident Children",
    "prompt": "Design a confidence-building parenting approach with autonomy support, challenge calibration, failure response, praise strategy, and identity development for:"
  },
  {
    "id": 646,
    "category": "parenting",
    "title": "Financial Literacy for Kids",
    "prompt": "Design an age-appropriate financial literacy program for children covering earning, saving, spending, giving, investing, and entrepreneurship for:"
  },
  {
    "id": 647,
    "category": "parenting",
    "title": "College Preparation",
    "prompt": "Design a comprehensive college preparation plan starting in middle school covering academics, extracurriculars, testing, applications, financial planning, and launch for:"
  },
  {
    "id": 648,
    "category": "parenting",
    "title": "Managing Childhood Anxiety",
    "prompt": "Design a parent's guide to supporting anxious children with validation, graduated exposure, school collaboration, professional support, and self-care for parents for:"
  },
  {
    "id": 649,
    "category": "parenting",
    "title": "Gifted Child Support",
    "prompt": "Design a comprehensive support plan for gifted children covering intellectual challenge, emotional intensity, social connections, underachievement prevention, and advocacy for:"
  },
  {
    "id": 650,
    "category": "parenting",
    "title": "Special Needs Parenting",
    "prompt": "Design a support framework for parents of children with special needs covering educational advocacy, therapy coordination, sibling support, and parent self-care for:"
  },
  {
    "id": 651,
    "category": "parenting",
    "title": "Teenage Communication",
    "prompt": "Design a communication strategy for maintaining connection with teenagers covering listening techniques, conflict navigation, boundary setting, and relationship preservation for:"
  },
  {
    "id": 652,
    "category": "parenting",
    "title": "Family Values",
    "prompt": "Design a process for identifying, articulating, and living family values with rituals, traditions, decision-making, and intentional culture building for:"
  },
  {
    "id": 653,
    "category": "parenting",
    "title": "Child Sleep Training",
    "prompt": "Design an age-appropriate sleep training and healthy sleep habits program with routine development, environment optimization, and common challenge solutions for:"
  },
  {
    "id": 654,
    "category": "parenting",
    "title": "Multicultural Parenting",
    "prompt": "Design a multicultural family strategy that honors multiple cultural identities, preserves heritage languages, builds cultural pride, and navigates cultural conflicts for:"
  },
  {
    "id": 655,
    "category": "parenting",
    "title": "Co-Parenting After Divorce",
    "prompt": "Design a constructive co-parenting system after divorce with communication protocols, consistency between homes, child-centered decisions, and conflict minimization for:"
  },
  {
    "id": 656,
    "category": "parenting",
    "title": "Raising Boys",
    "prompt": "Design a raising boys program addressing emotional intelligence, masculinity, communication, relationships, purpose, and positive male identity for:"
  },
  {
    "id": 657,
    "category": "parenting",
    "title": "Raising Girls",
    "prompt": "Design a raising girls program addressing confidence, body image, STEM, relationships, assertiveness, and positive female identity and leadership for:"
  },
  {
    "id": 658,
    "category": "parenting",
    "title": "Digital Age Parenting",
    "prompt": "Design a comprehensive digital parenting strategy covering online safety, social media, gaming, digital citizenship, privacy, and technology-life balance for:"
  },
  {
    "id": 659,
    "category": "parenting",
    "title": "Attachment Parenting",
    "prompt": "Design an attachment parenting approach with responsiveness, connection rituals, independence building, and transition to school-age attachment for:"
  },
  {
    "id": 660,
    "category": "parenting",
    "title": "Family Meetings",
    "prompt": "Design a family meeting system with regular check-ins, problem-solving protocols, celebration rituals, planning, and age-appropriate participation for:"
  },
  {
    "id": 661,
    "category": "parenting",
    "title": "Chores and Responsibility",
    "prompt": "Design an age-appropriate chore and responsibility system that builds work ethic, family contribution, competence, and intrinsic motivation for children aged:"
  },
  {
    "id": 662,
    "category": "parenting",
    "title": "Summer Learning Prevention",
    "prompt": "Design an engaging summer learning prevention program that maintains academic skills, encourages exploration, builds independence, and avoids burnout for:"
  },
  {
    "id": 663,
    "category": "environment",
    "title": "Personal Sustainability Plan",
    "prompt": "Design a comprehensive personal sustainability plan covering energy, transportation, food, consumption, water, waste, and community action for someone in:"
  },
  {
    "id": 664,
    "category": "environment",
    "title": "Business Sustainability Strategy",
    "prompt": "Develop a complete business sustainability strategy with environmental assessment, reduction targets, circular economy integration, reporting, and stakeholder communication for:"
  },
  {
    "id": 665,
    "category": "environment",
    "title": "Carbon Footprint Reduction",
    "prompt": "Design a systematic carbon footprint reduction plan with current assessment, highest-impact changes, offset strategy, and progress tracking for:"
  },
  {
    "id": 666,
    "category": "environment",
    "title": "Renewable Energy Transition",
    "prompt": "Design a renewable energy transition plan for a home or business with assessment, technology selection, financial analysis, installation, and optimization for:"
  },
  {
    "id": 667,
    "category": "environment",
    "title": "Zero Waste Program",
    "prompt": "Design a zero waste program with waste audit, reduction hierarchy, composting, recycling optimization, procurement changes, and measurement for:"
  },
  {
    "id": 668,
    "category": "environment",
    "title": "Biodiversity Conservation",
    "prompt": "Design a local biodiversity conservation program with habitat assessment, restoration activities, species monitoring, community engagement, and funding for:"
  },
  {
    "id": 669,
    "category": "environment",
    "title": "Climate Change Adaptation",
    "prompt": "Design a climate change adaptation plan for a community or organization with vulnerability assessment, risk prioritization, adaptation measures, and monitoring for:"
  },
  {
    "id": 670,
    "category": "environment",
    "title": "Sustainable Food System",
    "prompt": "Design a sustainable food system strategy covering plant-forward eating, local sourcing, food waste reduction, growing food, and food system advocacy for:"
  },
  {
    "id": 671,
    "category": "environment",
    "title": "Water Conservation",
    "prompt": "Design a comprehensive water conservation program with audit, efficiency measures, rainwater harvesting, landscaping, and behavioral change for:"
  },
  {
    "id": 672,
    "category": "environment",
    "title": "Environmental Education",
    "prompt": "Design an environmental education program that builds ecological literacy, connection to nature, systems thinking, and action orientation for:"
  },
  {
    "id": 673,
    "category": "environment",
    "title": "Corporate ESG Strategy",
    "prompt": "Develop a comprehensive ESG strategy with materiality assessment, goal setting, reporting framework, stakeholder engagement, and governance for:"
  },
  {
    "id": 674,
    "category": "environment",
    "title": "Circular Economy Design",
    "prompt": "Design a circular economy business model with product design, material flows, reverse logistics, remanufacturing, and ecosystem partnerships for:"
  },
  {
    "id": 675,
    "category": "environment",
    "title": "Urban Greening",
    "prompt": "Design an urban greening strategy with green infrastructure, urban forests, green roofs, community gardens, and biodiversity corridors for:"
  },
  {
    "id": 676,
    "category": "environment",
    "title": "Climate Communication",
    "prompt": "Design a climate communication strategy that increases engagement, reduces denial, inspires action, and builds climate hope for:"
  },
  {
    "id": 677,
    "category": "environment",
    "title": "Environmental Justice",
    "prompt": "Design an environmental justice program addressing disproportionate environmental burdens on marginalized communities with advocacy, remediation, and policy change for:"
  },
  {
    "id": 678,
    "category": "environment",
    "title": "Sustainable Agriculture",
    "prompt": "Design a sustainable agriculture transition plan with regenerative practices, soil health, water management, biodiversity, and economic viability for:"
  },
  {
    "id": 679,
    "category": "environment",
    "title": "Ocean Conservation",
    "prompt": "Design an ocean conservation program with plastic reduction, marine protected areas, sustainable seafood, coastal restoration, and awareness building for:"
  },
  {
    "id": 680,
    "category": "environment",
    "title": "Green Building",
    "prompt": "Design a green building project with energy efficiency, material selection, water conservation, indoor air quality, and certification pathway for:"
  },
  {
    "id": 681,
    "category": "environment",
    "title": "Environmental Policy",
    "prompt": "Write a compelling environmental policy brief with scientific evidence, economic analysis, co-benefits, implementation pathway, and political strategy for:"
  },
  {
    "id": 682,
    "category": "environment",
    "title": "Community Resilience",
    "prompt": "Design a community climate resilience plan with vulnerability mapping, adaptation projects, emergency preparedness, social cohesion, and funding strategy for:"
  },
  {
    "id": 683,
    "category": "environment",
    "title": "Ecosystem Services",
    "prompt": "Design an ecosystem services valuation and protection program with service identification, economic quantification, payment mechanisms, and governance for:"
  },
  {
    "id": 684,
    "category": "environment",
    "title": "Wildlife Conservation",
    "prompt": "Design a wildlife conservation program with species assessment, habitat protection, human-wildlife conflict mitigation, community engagement, and monitoring for:"
  },
  {
    "id": 685,
    "category": "environment",
    "title": "Sustainable Tourism",
    "prompt": "Design a sustainable tourism strategy with carrying capacity management, local benefit maximization, environmental protection, and visitor education for:"
  },
  {
    "id": 686,
    "category": "environment",
    "title": "Environmental Monitoring",
    "prompt": "Design an environmental monitoring program with indicator selection, data collection methods, analysis, reporting, and adaptive management for:"
  },
  {
    "id": 687,
    "category": "environment",
    "title": "Climate Change Mitigation",
    "prompt": "Design a comprehensive climate change mitigation strategy with emission reduction across sectors, technology deployment, land use, and international cooperation for:"
  },
  {
    "id": 688,
    "category": "science",
    "title": "Physics Explainer",
    "prompt": "Explain the following physics concept from first principles, using mathematical derivation where appropriate, real-world applications, historical discovery story, and common misconceptions:"
  },
  {
    "id": 689,
    "category": "science",
    "title": "Chemistry Process",
    "prompt": "Describe the following chemical process with molecular-level explanation, reaction mechanisms, industrial applications, safety considerations, and environmental impact:"
  },
  {
    "id": 690,
    "category": "science",
    "title": "Biology System",
    "prompt": "Explain the following biological system with evolutionary context, molecular mechanisms, clinical relevance, recent research advances, and open questions:"
  },
  {
    "id": 691,
    "category": "science",
    "title": "Astronomy Concept",
    "prompt": "Explain the following astronomy or cosmology concept with observational evidence, mathematical framework, implications for our understanding of the universe, and future research:"
  },
  {
    "id": 692,
    "category": "science",
    "title": "Neuroscience Topic",
    "prompt": "Explain the following neuroscience concept with brain regions involved, neural mechanisms, behavioral implications, clinical connections, and cutting-edge research:"
  },
  {
    "id": 693,
    "category": "science",
    "title": "Environmental Science",
    "prompt": "Analyze the following environmental science topic with ecological principles, human impacts, feedback loops, monitoring methods, and intervention strategies:"
  },
  {
    "id": 694,
    "category": "science",
    "title": "Genetics and Genomics",
    "prompt": "Explain the following genetics or genomics concept with molecular mechanisms, inheritance patterns, clinical applications, ethical implications, and recent advances:"
  },
  {
    "id": 695,
    "category": "science",
    "title": "Materials Science",
    "prompt": "Explain the following materials science concept with atomic structure, properties, processing methods, applications, and current research frontiers:"
  },
  {
    "id": 696,
    "category": "science",
    "title": "Mathematical Proof",
    "prompt": "Write a complete mathematical proof for the following theorem with motivation, setup, step-by-step derivation, geometric intuition where applicable, and applications:"
  },
  {
    "id": 697,
    "category": "science",
    "title": "Scientific Debate",
    "prompt": "Present both sides of the following scientific controversy with the evidence for each position, methodological critiques, expert consensus status, and unresolved questions:"
  },
  {
    "id": 698,
    "category": "science",
    "title": "Emerging Technology Science",
    "prompt": "Explain the scientific principles underlying the following emerging technology with current capabilities, fundamental limits, research challenges, and timeline expectations:"
  },
  {
    "id": 699,
    "category": "science",
    "title": "Bioethics Case",
    "prompt": "Analyze the following bioethics case with stakeholder perspectives, ethical principles in tension, regulatory context, precedent cases, and recommended resolution:"
  },
  {
    "id": 700,
    "category": "technology",
    "title": "AI Ethics Framework",
    "prompt": "Develop a comprehensive AI ethics framework with fairness, accountability, transparency, privacy, safety, and human oversight principles applied to:"
  },
  {
    "id": 701,
    "category": "technology",
    "title": "Machine Learning Pipeline",
    "prompt": "Design a complete ML pipeline with data collection, preprocessing, feature engineering, model selection, training, evaluation, deployment, and monitoring for:"
  },
  {
    "id": 702,
    "category": "technology",
    "title": "Natural Language Processing",
    "prompt": "Design an NLP application with task definition, data requirements, model selection, training approach, evaluation metrics, and deployment architecture for:"
  },
  {
    "id": 703,
    "category": "technology",
    "title": "Computer Vision System",
    "prompt": "Design a computer vision system with task specification, dataset requirements, architecture selection, training strategy, and deployment for:"
  },
  {
    "id": 704,
    "category": "technology",
    "title": "Recommendation Engine",
    "prompt": "Design a recommendation engine with algorithm selection, data requirements, cold start handling, evaluation metrics, and business integration for:"
  },
  {
    "id": 705,
    "category": "technology",
    "title": "Autonomous Systems",
    "prompt": "Design an autonomous system architecture with perception, planning, control, safety, human oversight, and testing framework for:"
  },
  {
    "id": 706,
    "category": "technology",
    "title": "Distributed Systems",
    "prompt": "Design a distributed system with consistency model, fault tolerance, scalability, partition handling, and operational complexity trade-offs for:"
  },
  {
    "id": 707,
    "category": "technology",
    "title": "Real-Time Systems",
    "prompt": "Design a real-time processing system with latency requirements, architecture, data flow, scaling strategy, and monitoring for:"
  },
  {
    "id": 708,
    "category": "technology",
    "title": "Platform Engineering",
    "prompt": "Design a platform engineering capability with internal developer platform, golden paths, self-service infrastructure, and developer experience metrics for:"
  },
  {
    "id": 709,
    "category": "technology",
    "title": "Technology Ethics",
    "prompt": "Analyze the ethical implications of the following technology with stakeholder impacts, regulatory considerations, mitigation strategies, and governance recommendations for:"
  },
  {
    "id": 710,
    "category": "psychology",
    "title": "ACT Therapy Concepts",
    "prompt": "Design an Acceptance and Commitment Therapy (ACT) based intervention with defusion, acceptance, present-moment, values, committed action, and flexible perspective for:"
  },
  {
    "id": 711,
    "category": "psychology",
    "title": "Schema Therapy",
    "prompt": "Apply schema therapy concepts with early maladaptive schema identification, mode work, limited reparenting, and behavioral pattern change for:"
  },
  {
    "id": 712,
    "category": "psychology",
    "title": "Dialectical Behavior Therapy",
    "prompt": "Design a DBT-informed skills program with mindfulness, distress tolerance, emotional regulation, and interpersonal effectiveness for:"
  },
  {
    "id": 713,
    "category": "psychology",
    "title": "Narrative Therapy",
    "prompt": "Apply narrative therapy techniques with externalizing problems, unique outcomes, re-authoring, and alternative story development for:"
  },
  {
    "id": 714,
    "category": "psychology",
    "title": "Solution-Focused Therapy",
    "prompt": "Design a solution-focused approach with miracle question, scaling, exceptions, coping questions, and strength-based goal setting for:"
  },
  {
    "id": 715,
    "category": "psychology",
    "title": "Attachment Theory Application",
    "prompt": "Apply attachment theory to improve relationships, parenting, therapy, or organizational dynamics with specific attachment style interventions for:"
  },
  {
    "id": 716,
    "category": "psychology",
    "title": "Grief and Loss",
    "prompt": "Design a grief support program using contemporary grief theory with meaning reconstruction, continuing bonds, and post-traumatic growth for:"
  },
  {
    "id": 717,
    "category": "psychology",
    "title": "Perfectionism Treatment",
    "prompt": "Design a perfectionism treatment program with psychoeducation, cost-benefit analysis, behavioral experiments, self-compassion, and relapse prevention for:"
  },
  {
    "id": 718,
    "category": "psychology",
    "title": "Procrastination Intervention",
    "prompt": "Design a comprehensive procrastination intervention addressing emotional regulation, temporal motivation, implementation intentions, and accountability for:"
  },
  {
    "id": 719,
    "category": "psychology",
    "title": "Imposter Syndrome",
    "prompt": "Design an imposter syndrome intervention program with cognitive restructuring, evidence-based self-assessment, community building, and internalization for:"
  },
  {
    "id": 720,
    "category": "career",
    "title": "Executive Coaching",
    "prompt": "Design an executive coaching program with assessment, goal setting, session structure, accountability, and measuring leadership behavior change for:"
  },
  {
    "id": 721,
    "category": "career",
    "title": "Workplace Bullying Response",
    "prompt": "Design a comprehensive response to workplace bullying with documentation, HR escalation, legal considerations, support resources, and career protection for:"
  },
  {
    "id": 722,
    "category": "career",
    "title": "Remote Leadership",
    "prompt": "Design a remote leadership strategy with presence without micromanagement, team cohesion, performance management, culture building, and career development for:"
  },
  {
    "id": 723,
    "category": "career",
    "title": "Cross-Cultural Leadership",
    "prompt": "Design a cross-cultural leadership approach with cultural intelligence development, communication adaptation, and inclusive team management for:"
  },
  {
    "id": 724,
    "category": "career",
    "title": "Career Plateau Breakthrough",
    "prompt": "Design a strategy for breaking through a career plateau with honest diagnosis, network activation, skill differentiation, and momentum building for:"
  },
  {
    "id": 725,
    "category": "career",
    "title": "Interview Rejection Recovery",
    "prompt": "Design a constructive interview rejection recovery process with feedback gathering, gap analysis, narrative improvement, and resilience building for:"
  },
  {
    "id": 726,
    "category": "career",
    "title": "Building a Board Network",
    "prompt": "Design a strategy for building relationships with board directors and non-executive directors for career advancement and business development for:"
  },
  {
    "id": 727,
    "category": "career",
    "title": "Authentic Leadership",
    "prompt": "Develop an authentic leadership development program with self-awareness, values alignment, genuine communication, and sustainable energy for:"
  },
  {
    "id": 728,
    "category": "career",
    "title": "Organizational Navigation",
    "prompt": "Design a strategy for navigating organizational politics ethically with stakeholder mapping, influence building, and authentic relationship development for:"
  },
  {
    "id": 729,
    "category": "career",
    "title": "Career Brand Management",
    "prompt": "Design a comprehensive career brand management system with reputation building, visibility strategy, thought leadership, and brand consistency for:"
  },
  {
    "id": 730,
    "category": "finance",
    "title": "Options Trading",
    "prompt": "Design a disciplined options trading strategy with risk management, position sizing, strategy selection, Greeks understanding, and exit rules for:"
  },
  {
    "id": 731,
    "category": "finance",
    "title": "Tax-Loss Harvesting",
    "prompt": "Design a systematic tax-loss harvesting program with trigger rules, wash sale avoidance, tax-efficient rebalancing, and annual review for:"
  },
  {
    "id": 732,
    "category": "finance",
    "title": "Family Office Setup",
    "prompt": "Design a family office structure with governance, investment policy, family education, philanthropic strategy, and generational transition for:"
  },
  {
    "id": 733,
    "category": "finance",
    "title": "Startup Equity",
    "prompt": "Navigate startup equity compensation with option types, vesting schedules, strike price, exercise strategy, tax optimization, and negotiation for:"
  },
  {
    "id": 734,
    "category": "finance",
    "title": "Income Statement Analysis",
    "prompt": "Teach comprehensive income statement analysis with revenue quality, margin trends, non-recurring items, segment analysis, and competitive benchmarking for:"
  },
  {
    "id": 735,
    "category": "finance",
    "title": "Balance Sheet Mastery",
    "prompt": "Teach comprehensive balance sheet analysis with liquidity ratios, leverage analysis, working capital, asset quality, and off-balance-sheet items for:"
  },
  {
    "id": 736,
    "category": "finance",
    "title": "Cash Flow Analysis",
    "prompt": "Teach comprehensive cash flow statement analysis with operating quality, capex assessment, free cash flow, and sustainability evaluation for:"
  },
  {
    "id": 737,
    "category": "finance",
    "title": "Dividend Investing",
    "prompt": "Design a dividend investing strategy with yield vs growth balance, payout ratio analysis, dividend safety scoring, and portfolio construction for:"
  },
  {
    "id": 738,
    "category": "finance",
    "title": "Real Estate Tax",
    "prompt": "Design a real estate tax optimization strategy covering depreciation, 1031 exchanges, opportunity zones, cost segregation, and entity structure for:"
  },
  {
    "id": 739,
    "category": "finance",
    "title": "Private Equity",
    "prompt": "Explain private equity investing with fund structures, deal sourcing, value creation, exit strategies, and return expectations for:"
  },
  {
    "id": 740,
    "category": "health",
    "title": "Pre-Diabetes Reversal",
    "prompt": "Design a lifestyle medicine program for pre-diabetes reversal with nutrition, exercise, weight management, sleep, stress, and monitoring for:"
  },
  {
    "id": 741,
    "category": "health",
    "title": "Autoimmune Disease Management",
    "prompt": "Design a comprehensive autoimmune disease lifestyle management program with anti-inflammatory nutrition, stress management, sleep, and medical coordination for:"
  },
  {
    "id": 742,
    "category": "health",
    "title": "Cancer Prevention",
    "prompt": "Design a cancer prevention lifestyle program based on current evidence covering nutrition, exercise, sleep, stress, alcohol, tobacco, and screening for:"
  },
  {
    "id": 743,
    "category": "health",
    "title": "Heart Disease Prevention",
    "prompt": "Design a comprehensive cardiovascular disease prevention program with risk factor management, lifestyle optimization, and medical monitoring for:"
  },
  {
    "id": 744,
    "category": "health",
    "title": "Diabetes Management",
    "prompt": "Design a comprehensive type 2 diabetes management program with nutrition, exercise, blood sugar monitoring, medication adherence, and complication prevention for:"
  },
  {
    "id": 745,
    "category": "health",
    "title": "Chronic Fatigue Management",
    "prompt": "Design a chronic fatigue management program with pacing, graded activity, sleep optimization, cognitive load management, and quality of life improvement for:"
  },
  {
    "id": 746,
    "category": "health",
    "title": "Migraine Management",
    "prompt": "Design a comprehensive migraine management program with trigger identification, preventive strategies, acute treatment, lifestyle optimization, and medical coordination for:"
  },
  {
    "id": 747,
    "category": "health",
    "title": "ADHD Management",
    "prompt": "Design a comprehensive ADHD management program with environmental design, routine building, cognitive strategies, exercise, nutrition, and medical coordination for:"
  },
  {
    "id": 748,
    "category": "health",
    "title": "Menopause Transition",
    "prompt": "Design a comprehensive menopause transition support program with symptom management, bone health, cardiovascular health, mental wellbeing, and relationships for:"
  },
  {
    "id": 749,
    "category": "health",
    "title": "Addiction Science",
    "prompt": "Design an evidence-based addiction recovery program using neuroscience principles with craving management, trigger avoidance, reward system restoration, and relapse prevention for:"
  },
  {
    "id": 750,
    "category": "marketing",
    "title": "TikTok Strategy",
    "prompt": "Develop a comprehensive TikTok marketing strategy with content formats, trend leveraging, creator partnerships, paid amplification, and analytics for:"
  },
  {
    "id": 751,
    "category": "marketing",
    "title": "Podcast Launch",
    "prompt": "Design a complete podcast launch strategy with show concept, format, production quality, distribution, launch marketing, and growth for:"
  },
  {
    "id": 752,
    "category": "marketing",
    "title": "Newsletter Growth",
    "prompt": "Design a newsletter growth strategy with content differentiation, acquisition channels, referral mechanics, retention, and monetization for:"
  },
  {
    "id": 753,
    "category": "marketing",
    "title": "YouTube SEO",
    "prompt": "Develop a YouTube SEO and growth strategy with keyword research, title optimization, thumbnail design, description, community building, and algorithm optimization for:"
  },
  {
    "id": 754,
    "category": "marketing",
    "title": "Customer Avatar",
    "prompt": "Create an ultra-detailed customer avatar with demographics, psychographics, buying triggers, objections, media consumption, and emotional drivers for:"
  },
  {
    "id": 755,
    "category": "marketing",
    "title": "Storytelling Framework",
    "prompt": "Develop a brand storytelling framework with story types, narrative structure, emotional arc, character development, and multi-channel adaptation for:"
  },
  {
    "id": 756,
    "category": "marketing",
    "title": "Pricing Psychology",
    "prompt": "Apply pricing psychology principles including anchoring, decoy pricing, charm pricing, bundling, and loss framing to optimize conversion for:"
  },
  {
    "id": 757,
    "category": "marketing",
    "title": "Word of Mouth Marketing",
    "prompt": "Design a word of mouth marketing program with remarkable experience design, referral triggers, social currency, practical value, and amplification for:"
  },
  {
    "id": 758,
    "category": "marketing",
    "title": "B2B Content Marketing",
    "prompt": "Develop a B2B content marketing strategy with thought leadership, SEO, lead generation, sales enablement, and pipeline influence for:"
  },
  {
    "id": 759,
    "category": "marketing",
    "title": "Marketing Technology Stack",
    "prompt": "Design an optimal marketing technology stack with core platforms, integration architecture, data flow, vendor selection, and ROI measurement for:"
  },
  {
    "id": 760,
    "category": "design",
    "title": "Design Research Methods",
    "prompt": "Design a mixed-methods design research program with qualitative and quantitative methods, synthesis approach, insight generation, and design implications for:"
  },
  {
    "id": 761,
    "category": "design",
    "title": "Service Blueprint",
    "prompt": "Create a detailed service blueprint with customer actions, frontstage employee actions, backstage employee actions, support processes, and improvement opportunities for:"
  },
  {
    "id": 762,
    "category": "design",
    "title": "Jobs To Be Done",
    "prompt": "Apply the Jobs-to-be-Done framework to understand customer motivations with job identification, outcome mapping, solution design, and messaging implications for:"
  },
  {
    "id": 763,
    "category": "design",
    "title": "Experience Mapping",
    "prompt": "Create a comprehensive experience map with phases, customer actions, thoughts, emotions, touchpoints, and opportunity areas for:"
  },
  {
    "id": 764,
    "category": "design",
    "title": "Concept Testing",
    "prompt": "Design a concept testing methodology with stimulus creation, participant recruitment, data collection, analysis, and iteration process for:"
  },
  {
    "id": 765,
    "category": "design",
    "title": "Interaction Design Patterns",
    "prompt": "Document interaction design patterns with context, problem, solution, examples, and implementation considerations for:"
  },
  {
    "id": 766,
    "category": "design",
    "title": "Visual Storytelling",
    "prompt": "Design a visual storytelling system with narrative structure, information hierarchy, data visualization, imagery, and emotional journey for:"
  },
  {
    "id": 767,
    "category": "design",
    "title": "Accessibility Testing",
    "prompt": "Design a comprehensive accessibility testing program with automated tools, manual testing, assistive technology testing, and remediation tracking for:"
  },
  {
    "id": 768,
    "category": "design",
    "title": "Design Language",
    "prompt": "Develop a design language with philosophical foundation, visual vocabulary, interaction vocabulary, voice and tone, and evolution process for:"
  },
  {
    "id": 769,
    "category": "design",
    "title": "Co-Design Facilitation",
    "prompt": "Design a co-design workshop with participant selection, activity sequence, facilitation techniques, synthesis process, and output integration for:"
  },
  {
    "id": 770,
    "category": "coding",
    "title": "Functional Programming",
    "prompt": "Rewrite the following code using functional programming principles with pure functions, immutability, function composition, and monads where appropriate:"
  },
  {
    "id": 771,
    "category": "coding",
    "title": "Clean Code Principles",
    "prompt": "Apply Clean Code principles to the following codebase with naming, functions, comments, formatting, error handling, and boundary management:"
  },
  {
    "id": 772,
    "category": "coding",
    "title": "Distributed System Patterns",
    "prompt": "Implement the following distributed system patterns with saga, CQRS, event sourcing, circuit breaker, and bulkhead for the following use case:"
  },
  {
    "id": 773,
    "category": "coding",
    "title": "Domain-Driven Design",
    "prompt": "Apply Domain-Driven Design to the following problem with bounded contexts, aggregates, domain events, repositories, and ubiquitous language for:"
  },
  {
    "id": 774,
    "category": "coding",
    "title": "Reactive Programming",
    "prompt": "Implement reactive programming patterns with observables, operators, backpressure, error handling, and testing for the following scenario:"
  },
  {
    "id": 775,
    "category": "coding",
    "title": "Low-Code No-Code",
    "prompt": "Design a low-code/no-code solution architecture with platform selection, integration approach, governance, citizen developer enablement, and limitations for:"
  },
  {
    "id": 776,
    "category": "coding",
    "title": "Open Source Contribution",
    "prompt": "Design a strategy for becoming a meaningful open source contributor with project selection, first contributions, community building, and maintainer path for:"
  },
  {
    "id": 777,
    "category": "coding",
    "title": "Programming Language Learning",
    "prompt": "Design an accelerated programming language learning program with core concepts, project-based practice, community, and integration with existing skills for:"
  },
  {
    "id": 778,
    "category": "coding",
    "title": "Legacy System Modernization",
    "prompt": "Design a legacy system modernization strategy with strangler fig pattern, incremental migration, risk mitigation, and team capability building for:"
  },
  {
    "id": 779,
    "category": "coding",
    "title": "Developer Experience",
    "prompt": "Design a developer experience improvement program with tooling, documentation, onboarding, feedback loops, and measuring developer productivity for:"
  },
  {
    "id": 780,
    "category": "business",
    "title": "Customer Discovery",
    "prompt": "Design a comprehensive customer discovery process with hypothesis formation, interview guide, experiment design, insight synthesis, and pivot criteria for:"
  },
  {
    "id": 781,
    "category": "business",
    "title": "Business Model Innovation",
    "prompt": "Design a business model innovation process with current model mapping, opportunity identification, prototype design, validation, and transition planning for:"
  },
  {
    "id": 782,
    "category": "business",
    "title": "Organizational Design",
    "prompt": "Design an organizational structure with reporting lines, spans of control, team topologies, decision rights, and coordination mechanisms for:"
  },
  {
    "id": 783,
    "category": "business",
    "title": "Culture Change",
    "prompt": "Design a culture change program with current culture diagnosis, desired culture articulation, behavior modeling, system alignment, and measurement for:"
  },
  {
    "id": 784,
    "category": "business",
    "title": "Strategic Alliance",
    "prompt": "Design a strategic alliance framework with partner selection, value exchange, governance structure, joint activities, and exit provisions for:"
  },
  {
    "id": 785,
    "category": "business",
    "title": "Pricing Optimization",
    "prompt": "Design a pricing optimization program with price elasticity research, competitive analysis, value metric selection, and monetization model for:"
  },
  {
    "id": 786,
    "category": "business",
    "title": "Customer Advisory Board",
    "prompt": "Design a customer advisory board program with member selection, meeting cadence, agenda design, insight integration, and member recognition for:"
  },
  {
    "id": 787,
    "category": "business",
    "title": "Business Intelligence",
    "prompt": "Design a business intelligence strategy with data infrastructure, reporting hierarchy, self-service analytics, data literacy, and governance for:"
  },
  {
    "id": 788,
    "category": "business",
    "title": "Startup Scaling",
    "prompt": "Design a startup scaling playbook covering team building, process development, culture preservation, systems implementation, and leadership evolution for:"
  },
  {
    "id": 789,
    "category": "business",
    "title": "Social Enterprise",
    "prompt": "Design a social enterprise business model that generates both social impact and financial sustainability with theory of change, revenue model, and impact measurement for:"
  },
  {
    "id": 790,
    "category": "writing",
    "title": "Newsletter Subject Lines",
    "prompt": "Write 20 high-open-rate email subject lines using curiosity gaps, personalization, urgency, social proof, and benefit-led techniques for:"
  },
  {
    "id": 791,
    "category": "writing",
    "title": "Viral Twitter Thread",
    "prompt": "Write a viral Twitter/X thread with a strong hook, progressive revelation, surprising insights, engagement questions, and powerful conclusion about:"
  },
  {
    "id": 792,
    "category": "writing",
    "title": "Amazon Book Description",
    "prompt": "Write a compelling Amazon book description with hook, pain point, promise, preview, credibility, and strong CTA for:"
  },
  {
    "id": 793,
    "category": "writing",
    "title": "YouTube Description",
    "prompt": "Write an SEO-optimized YouTube video description with keyword placement, timestamps, links, call to action, and hashtags for:"
  },
  {
    "id": 794,
    "category": "writing",
    "title": "Podcast Episode Description",
    "prompt": "Write a compelling podcast episode description with hook, key topics, guest intro, listener takeaways, and show notes outline for:"
  },
  {
    "id": 795,
    "category": "writing",
    "title": "Cold Email Sequence",
    "prompt": "Write a 5-email cold email sequence with subject lines, personalized openers, value propositions, social proof, and CTAs for:"
  },
  {
    "id": 796,
    "category": "writing",
    "title": "Testimonial Collection",
    "prompt": "Write a testimonial collection system with request templates, guiding questions, follow-up, and social proof optimization for:"
  },
  {
    "id": 797,
    "category": "writing",
    "title": "Website Homepage Copy",
    "prompt": "Write compelling homepage copy with above-the-fold headline, subheadline, value proposition, social proof, features, and CTA for:"
  },
  {
    "id": 798,
    "category": "writing",
    "title": "Video Sales Letter",
    "prompt": "Write a complete video sales letter script with attention, interest, desire, proof, offer, urgency, and guarantee for:"
  },
  {
    "id": 799,
    "category": "writing",
    "title": "Webinar Promotional Email",
    "prompt": "Write a promotional email sequence (3 emails) for a webinar with subject lines, benefits, urgency, and registration CTA for:"
  },
  {
    "id": 800,
    "category": "writing",
    "title": "Instagram Caption",
    "prompt": "Write 10 engaging Instagram captions with hooks, storytelling, value, personality, and CTAs for different post types about:"
  },
  {
    "id": 801,
    "category": "writing",
    "title": "Bio Writing",
    "prompt": "Write a compelling bio in 3 lengths (tweet, paragraph, full page) that positions you as an authority and connects with your target audience for:"
  },
  {
    "id": 802,
    "category": "creative",
    "title": "Short Film Script",
    "prompt": "Write a complete short film script (10-15 minutes) with compelling premise, visual storytelling, minimal dialogue, and emotional punch for:"
  },
  {
    "id": 803,
    "category": "creative",
    "title": "Game Narrative Design",
    "prompt": "Design a complete game narrative with world lore, main story arc, character backstories, branching dialogue, and environmental storytelling for:"
  },
  {
    "id": 804,
    "category": "creative",
    "title": "Podcast Fiction",
    "prompt": "Write an audio drama script with sound direction, voice acting notes, atmospheric writing, and compelling multi-episode arc for:"
  },
  {
    "id": 805,
    "category": "creative",
    "title": "Song Writing Workshop",
    "prompt": "Design a song writing workshop with chord progressions, lyric writing techniques, melody development, and arrangement for the genre of:"
  },
  {
    "id": 806,
    "category": "creative",
    "title": "Creative Writing Exercises",
    "prompt": "Design 20 creative writing exercises that build specific craft skills (show dont tell, subtext, pacing, voice, tension) for writers working on:"
  },
  {
    "id": 807,
    "category": "creative",
    "title": "Graphic Novel Outline",
    "prompt": "Create a complete graphic novel outline with chapter breakdown, panel description samples, visual metaphors, character design notes, and thematic arc for:"
  },
  {
    "id": 808,
    "category": "creative",
    "title": "Escape Room Design",
    "prompt": "Design a complete escape room experience with theme, puzzles, narrative, flow, hint system, and difficulty calibration for:"
  },
  {
    "id": 809,
    "category": "creative",
    "title": "Comedy Writing",
    "prompt": "Write comedy content (stand-up bit, sketch, or comedic essay) with setup, escalation, callbacks, and surprising payoff about:"
  },
  {
    "id": 810,
    "category": "creative",
    "title": "Travel Writing",
    "prompt": "Write a literary travel essay that captures place, culture, personal transformation, and universal meaning about:"
  },
  {
    "id": 811,
    "category": "creative",
    "title": "Food Writing",
    "prompt": "Write a food essay that captures flavor, culture, memory, and meaning through the lens of a specific dish, restaurant, or culinary tradition:"
  },
  {
    "id": 812,
    "category": "education",
    "title": "Mentorship Program Design",
    "prompt": "Design a structured mentorship program with matching criteria, onboarding, meeting cadence, goal setting, and program evaluation for:"
  },
  {
    "id": 813,
    "category": "education",
    "title": "Capstone Project Design",
    "prompt": "Design a rigorous capstone project with real-world problem, stakeholder partnership, interdisciplinary integration, and authentic assessment for:"
  },
  {
    "id": 814,
    "category": "education",
    "title": "Global Classroom",
    "prompt": "Design a global classroom project connecting students across countries with collaborative inquiry, cultural exchange, and shared creation for:"
  },
  {
    "id": 815,
    "category": "education",
    "title": "STEAM Integration",
    "prompt": "Design an integrated STEAM unit with art as the connective tissue across science, technology, engineering, and math for:"
  },
  {
    "id": 816,
    "category": "education",
    "title": "Student Voice Program",
    "prompt": "Design a student voice and agency program where students co-design curriculum, assess learning, and lead school improvement for:"
  },
  {
    "id": 817,
    "category": "education",
    "title": "Learning Analytics",
    "prompt": "Design a learning analytics approach using data to personalize instruction, predict challenges, and improve outcomes while protecting privacy for:"
  },
  {
    "id": 818,
    "category": "education",
    "title": "Character Education",
    "prompt": "Design a character education program that authentically develops virtues and ethical reasoning through curriculum integration and school culture for:"
  },
  {
    "id": 819,
    "category": "education",
    "title": "Design Thinking in School",
    "prompt": "Implement design thinking in a school context with challenge identification, empathy research, ideation, prototyping, and testing with real stakeholders for:"
  },
  {
    "id": 820,
    "category": "education",
    "title": "Outdoor Education",
    "prompt": "Design an outdoor education program that uses nature as classroom with experiential learning, ecological literacy, and risk management for:"
  },
  {
    "id": 821,
    "category": "education",
    "title": "Assessment Reform",
    "prompt": "Design an assessment reform initiative moving from grades to competency demonstration with evidence portfolios and growth tracking for:"
  },
  {
    "id": 822,
    "category": "productivity",
    "title": "Annual Planning Retreat",
    "prompt": "Design a personal annual planning retreat (1-2 days) with reflection exercises, vision work, goal setting, and implementation planning for:"
  },
  {
    "id": 823,
    "category": "productivity",
    "title": "Creative Sprint",
    "prompt": "Design a creative sprint methodology for producing focused creative output in compressed timeframes with ideation, production, and curation phases for:"
  },
  {
    "id": 824,
    "category": "productivity",
    "title": "Second Brain Setup",
    "prompt": "Design a complete Second Brain implementation using PARA method with capture tools, processing workflow, and knowledge retrieval for:"
  },
  {
    "id": 825,
    "category": "productivity",
    "title": "Decision Journal",
    "prompt": "Design a decision journal practice with decision documentation, reasoning capture, outcome tracking, and learning integration for:"
  },
  {
    "id": 826,
    "category": "productivity",
    "title": "Life Operating System",
    "prompt": "Design a complete personal life operating system with values, roles, goals, projects, habits, review cadences, and continuous improvement for:"
  },
  {
    "id": 827,
    "category": "productivity",
    "title": "Delegation Mastery",
    "prompt": "Design a delegation mastery system for executives and managers with task assessment, handoff protocols, progress monitoring, and capability building for:"
  },
  {
    "id": 828,
    "category": "productivity",
    "title": "Focus Blocks Design",
    "prompt": "Design an optimal deep work schedule with protected blocks, trigger rituals, distraction protocols, and sustainable creative output for:"
  },
  {
    "id": 829,
    "category": "productivity",
    "title": "Collaboration Charter",
    "prompt": "Design a team collaboration charter with communication norms, meeting culture, decision rights, conflict protocols, and accountability for:"
  },
  {
    "id": 830,
    "category": "productivity",
    "title": "Inbox Zero System",
    "prompt": "Design a complete inbox zero system across email, Slack, and other tools with triage rules, response templates, and maintenance habits for:"
  },
  {
    "id": 831,
    "category": "productivity",
    "title": "Annual Review Template",
    "prompt": "Design a comprehensive annual review process with reflection questions, metrics review, lessons learned, gratitude practice, and future planning for:"
  },
  {
    "id": 832,
    "category": "environment",
    "title": "Corporate Sustainability Report",
    "prompt": "Write a compelling corporate sustainability report with highlights, metrics, case studies, challenges, commitments, and stakeholder communication for:"
  },
  {
    "id": 833,
    "category": "environment",
    "title": "Environmental Impact Assessment",
    "prompt": "Design an environmental impact assessment process with baseline measurement, impact identification, mitigation hierarchy, and monitoring plan for:"
  },
  {
    "id": 834,
    "category": "environment",
    "title": "Plastic Reduction Program",
    "prompt": "Design a comprehensive plastic reduction program for a business or community with audit, alternatives, behavior change, and measurement for:"
  },
  {
    "id": 835,
    "category": "environment",
    "title": "Regenerative Business",
    "prompt": "Design a regenerative business framework that goes beyond sustainability to actively restore ecological and social systems for:"
  },
  {
    "id": 836,
    "category": "environment",
    "title": "Climate Action Plan",
    "prompt": "Design a comprehensive organizational climate action plan with emissions inventory, science-based targets, reduction roadmap, and reporting for:"
  },
  {
    "id": 837,
    "category": "environment",
    "title": "Biodiversity Net Gain",
    "prompt": "Design a biodiversity net gain strategy for a development project with baseline assessment, impact mitigation, offset design, and monitoring for:"
  },
  {
    "id": 838,
    "category": "environment",
    "title": "Circular Packaging",
    "prompt": "Design a circular packaging system with material selection, refill schemes, take-back programs, and consumer communication for:"
  },
  {
    "id": 839,
    "category": "environment",
    "title": "Sustainable Supply Chain",
    "prompt": "Design a sustainable supply chain program with supplier assessment, standards setting, capacity building, and transparency reporting for:"
  },
  {
    "id": 840,
    "category": "environment",
    "title": "Green Finance",
    "prompt": "Design a green finance strategy with ESG integration, green bonds, impact investment, climate risk assessment, and reporting for:"
  },
  {
    "id": 841,
    "category": "environment",
    "title": "Nature-Based Solutions",
    "prompt": "Design nature-based solutions for climate adaptation and mitigation with ecosystem selection, co-benefits, financing, and monitoring for:"
  },
  {
    "id": 842,
    "category": "parenting",
    "title": "Positive Reinforcement System",
    "prompt": "Design a positive reinforcement system that builds intrinsic motivation, catches children being good, and reduces punishment for:"
  },
  {
    "id": 843,
    "category": "parenting",
    "title": "Technology-Free Family Time",
    "prompt": "Design meaningful technology-free family activities and rituals that build connection, creativity, and lasting memories for:"
  },
  {
    "id": 844,
    "category": "parenting",
    "title": "Raising Anti-Racist Children",
    "prompt": "Design a framework for raising anti-racist children with age-appropriate conversations, diverse representation, active allyship, and ongoing learning for:"
  },
  {
    "id": 845,
    "category": "parenting",
    "title": "Nature Connection Parenting",
    "prompt": "Design a nature connection parenting approach with outdoor routines, nature play, ecological literacy, and adventure for:"
  },
  {
    "id": 846,
    "category": "parenting",
    "title": "Executive Function Development",
    "prompt": "Design activities and strategies to develop executive function skills (planning, self-control, working memory) in children aged:"
  },
  {
    "id": 847,
    "category": "parenting",
    "title": "Birth Order Parenting",
    "prompt": "Design parenting strategies that account for birth order dynamics while promoting each child's unique strengths and avoiding stereotypes for:"
  },
  {
    "id": 848,
    "category": "parenting",
    "title": "Parenting After Trauma",
    "prompt": "Design a trauma-informed parenting approach for parents who have experienced trauma, with self-regulation, breaking cycles, and healing for:"
  },
  {
    "id": 849,
    "category": "parenting",
    "title": "Father Involvement Program",
    "prompt": "Design a father involvement program with role definition, practical activities, maternal gatekeeping strategies, and community support for:"
  },
  {
    "id": 850,
    "category": "parenting",
    "title": "Bilingual Parenting",
    "prompt": "Design a bilingual parenting strategy with language exposure, language separation, community support, and identity development for:"
  },
  {
    "id": 851,
    "category": "parenting",
    "title": "Grandparent Integration",
    "prompt": "Design a strategy for integrating grandparents positively into child-rearing with role definition, communication, boundary setting, and value for:"
  },
  {
    "id": 852,
    "category": "travel",
    "title": "Travel Safety for Women",
    "prompt": "Design a comprehensive solo female travel safety system with destination research, accommodation, transportation, situational awareness, and community for:"
  },
  {
    "id": 853,
    "category": "travel",
    "title": "Slow Travel Philosophy",
    "prompt": "Design a slow travel approach that maximizes depth, local connection, personal growth, and environmental responsibility for:"
  },
  {
    "id": 854,
    "category": "travel",
    "title": "Working Holiday",
    "prompt": "Design a working holiday strategy with visa requirements, job search, accommodation, budget management, and experience maximization for:"
  },
  {
    "id": 855,
    "category": "travel",
    "title": "Transformative Travel",
    "prompt": "Design a transformative travel experience that creates lasting personal growth through immersion, challenge, service, and reflection for:"
  },
  {
    "id": 856,
    "category": "travel",
    "title": "Travel with Disabilities",
    "prompt": "Design accessible travel strategies with destination research, accommodation, transportation, support services, and community for travelers with:"
  },
  {
    "id": 857,
    "category": "travel",
    "title": "Food Tourism",
    "prompt": "Design a food tourism experience that uses cuisine as the primary lens for cultural exploration with markets, restaurants, cooking, and history for:"
  },
  {
    "id": 858,
    "category": "travel",
    "title": "Wildlife Tourism Ethics",
    "prompt": "Design an ethical wildlife tourism approach with operator vetting, interaction standards, photography ethics, and conservation contribution for:"
  },
  {
    "id": 859,
    "category": "travel",
    "title": "Urban Exploration",
    "prompt": "Design an urban exploration methodology for discovering authentic city life beyond tourist areas with neighborhood research, local guides, and documentation for:"
  },
  {
    "id": 860,
    "category": "travel",
    "title": "Travel Mental Health",
    "prompt": "Design a mental health support strategy for long-term travelers addressing loneliness, purpose, routine, relationships, and professional support for:"
  },
  {
    "id": 861,
    "category": "travel",
    "title": "Pilgrimage Planning",
    "prompt": "Design a meaningful pilgrimage experience with route selection, physical preparation, spiritual intention, walking practice, and integration for:"
  },
  {
    "id": 862,
    "category": "psychology",
    "title": "Mindset Coaching",
    "prompt": "Design a mindset coaching program with limiting belief identification, reframing techniques, new belief installation, and behavioral activation for:"
  },
  {
    "id": 863,
    "category": "psychology",
    "title": "Emotional Regulation Training",
    "prompt": "Design an emotional regulation training program with dysregulation awareness, window of tolerance, regulation techniques, and daily practice for:"
  },
  {
    "id": 864,
    "category": "psychology",
    "title": "Confidence Building",
    "prompt": "Design a systematic confidence building program with confidence anatomy, competence development, courage training, and social proof building for:"
  },
  {
    "id": 865,
    "category": "psychology",
    "title": "Self-Compassion Practice",
    "prompt": "Design a structured self-compassion program using Kristin Neff's model with mindfulness, common humanity, self-kindness, and integration for:"
  },
  {
    "id": 866,
    "category": "psychology",
    "title": "Stress Inoculation",
    "prompt": "Design a stress inoculation training program with education, skills acquisition, application training, and graduated exposure for:"
  },
  {
    "id": 867,
    "category": "psychology",
    "title": "Cognitive Load Management",
    "prompt": "Design a cognitive load management strategy with task complexity assessment, chunking, scaffolding, and cognitive offloading for:"
  },
  {
    "id": 868,
    "category": "psychology",
    "title": "Self-Determination",
    "prompt": "Apply self-determination theory to improve motivation with autonomy support, competence building, relatedness, and internalization for:"
  },
  {
    "id": 869,
    "category": "psychology",
    "title": "Psychological Flexibility",
    "prompt": "Design a psychological flexibility training program with ACT hexaflex processes, metaphors, exercises, and daily practice for:"
  },
  {
    "id": 870,
    "category": "psychology",
    "title": "Identity Development",
    "prompt": "Design an identity development program with exploration, commitment, narrative construction, and adaptive updating for:"
  },
  {
    "id": 871,
    "category": "psychology",
    "title": "Meaning Making",
    "prompt": "Design a meaning-making program using existential and positive psychology with purpose, significance, coherence, and engagement for:"
  },
  {
    "id": 872,
    "category": "science",
    "title": "Quantum Computing Explained",
    "prompt": "Explain quantum computing concepts from qubits through quantum advantage with analogies, current state, applications, and timeline for:"
  },
  {
    "id": 873,
    "category": "science",
    "title": "CRISPR Gene Editing",
    "prompt": "Explain CRISPR-Cas9 technology with mechanism, applications, ethical debates, current capabilities, limitations, and future directions:"
  },
  {
    "id": 874,
    "category": "science",
    "title": "Artificial Intelligence Science",
    "prompt": "Explain the scientific principles underlying modern AI with neural networks, training, emergent capabilities, and frontier research:"
  },
  {
    "id": 875,
    "category": "science",
    "title": "Space Colonization Science",
    "prompt": "Analyze the scientific challenges and solutions for space colonization covering life support, radiation, gravity, psychology, and technology for:"
  },
  {
    "id": 876,
    "category": "science",
    "title": "Ocean Science",
    "prompt": "Explain ocean science with physical oceanography, marine biology, climate role, deep sea exploration, and conservation for:"
  },
  {
    "id": 877,
    "category": "science",
    "title": "Consciousness Science",
    "prompt": "Explore the scientific approaches to understanding consciousness with neural correlates, integrated information theory, global workspace, and hard problem for:"
  },
  {
    "id": 878,
    "category": "science",
    "title": "Aging Science",
    "prompt": "Explain the science of aging with hallmarks, interventions, longevity research, emerging therapies, and lifestyle implications for:"
  },
  {
    "id": 879,
    "category": "science",
    "title": "Microbiome Science",
    "prompt": "Explain the microbiome with composition, function, gut-brain axis, disease connections, and modulation strategies for:"
  },
  {
    "id": 880,
    "category": "science",
    "title": "Clean Energy Science",
    "prompt": "Explain the science of clean energy technologies (solar, wind, storage, fusion, hydrogen) with mechanisms, efficiency, and scaling challenges for:"
  },
  {
    "id": 881,
    "category": "science",
    "title": "Pandemic Preparedness",
    "prompt": "Design a science-based pandemic preparedness framework with surveillance, rapid response, vaccine platform, communication, and global cooperation for:"
  },
  {
    "id": 882,
    "category": "technology",
    "title": "Quantum Safe Cryptography",
    "prompt": "Design a migration strategy to quantum-safe cryptography with algorithm selection, priority assessment, migration timeline, and testing for:"
  },
  {
    "id": 883,
    "category": "technology",
    "title": "Green Technology",
    "prompt": "Design a green technology strategy with energy efficiency, sustainable infrastructure, circular IT, and measuring environmental impact for:"
  },
  {
    "id": 884,
    "category": "technology",
    "title": "Digital Accessibility",
    "prompt": "Design a comprehensive digital accessibility program with WCAG compliance, assistive technology support, testing, and inclusive culture for:"
  },
  {
    "id": 885,
    "category": "technology",
    "title": "Technology Risk Management",
    "prompt": "Design a technology risk management framework with risk identification, assessment, treatment, monitoring, and governance for:"
  },
  {
    "id": 886,
    "category": "technology",
    "title": "Data Mesh Architecture",
    "prompt": "Design a data mesh architecture with domain ownership, data as product, self-serve platform, and federated governance for:"
  },
  {
    "id": 887,
    "category": "technology",
    "title": "Zero Trust Security",
    "prompt": "Design a zero trust security architecture with identity verification, device compliance, network segmentation, and continuous monitoring for:"
  },
  {
    "id": 888,
    "category": "technology",
    "title": "MLOps Implementation",
    "prompt": "Design a complete MLOps implementation with model registry, feature store, training pipelines, deployment, monitoring, and retraining for:"
  },
  {
    "id": 889,
    "category": "technology",
    "title": "Digital Product Management",
    "prompt": "Design a digital product management system with discovery, prioritization, delivery, measurement, and team structure for:"
  },
  {
    "id": 890,
    "category": "technology",
    "title": "Technology Debt Management",
    "prompt": "Design a technology debt management program with inventory, prioritization, remediation, prevention, and cultural change for:"
  },
  {
    "id": 891,
    "category": "technology",
    "title": "Enterprise Architecture",
    "prompt": "Design an enterprise architecture framework with business architecture, information architecture, application architecture, and technology architecture for:"
  },
  {
    "id": 892,
    "category": "coding",
    "title": "API Documentation",
    "prompt": "Write comprehensive API documentation with endpoint reference, authentication guide, code examples in 5 languages, error codes, and rate limiting for:"
  },
  {
    "id": 893,
    "category": "coding",
    "title": "Code Migration",
    "prompt": "Create a step-by-step code migration plan from one technology stack to another with risk assessment, testing strategy, and rollback plan for:"
  },
  {
    "id": 894,
    "category": "coding",
    "title": "Performance Profiling",
    "prompt": "Design a systematic performance profiling approach with tooling, bottleneck identification, optimization techniques, and benchmarking for:"
  },
  {
    "id": 895,
    "category": "coding",
    "title": "Code Standards",
    "prompt": "Develop a comprehensive code standards guide with naming conventions, formatting rules, documentation requirements, and review checklist for:"
  },
  {
    "id": 896,
    "category": "coding",
    "title": "Developer Onboarding",
    "prompt": "Design a developer onboarding program with codebase tour, architecture deep dives, mentorship, first tasks, and 30-60-90 day plan for:"
  },
  {
    "id": 897,
    "category": "coding",
    "title": "API Versioning",
    "prompt": "Design an API versioning strategy with version scheme, deprecation policy, migration guides, and backward compatibility for:"
  },
  {
    "id": 898,
    "category": "coding",
    "title": "Technical Roadmap",
    "prompt": "Create a technical roadmap with current state assessment, target architecture, migration plan, team requirements, and timeline for:"
  },
  {
    "id": 899,
    "category": "coding",
    "title": "Open API Design",
    "prompt": "Design a RESTful API following OpenAPI specification with resources, endpoints, request/response schemas, and error handling for:"
  },
  {
    "id": 900,
    "category": "coding",
    "title": "Event-Driven Architecture",
    "prompt": "Design an event-driven architecture with event taxonomy, message broker selection, event schema, consumer patterns, and observability for:"
  },
  {
    "id": 901,
    "category": "coding",
    "title": "Code Quality Metrics",
    "prompt": "Design a code quality measurement program with metrics selection, tooling, baselines, improvement targets, and team accountability for:"
  },
  {
    "id": 902,
    "category": "writing",
    "title": "Grant Writing Masterclass",
    "prompt": "Write a masterclass on grant writing with prospect research, relationship building, proposal structure, budget narrative, and follow-up for:"
  },
  {
    "id": 903,
    "category": "writing",
    "title": "Content Repurposing",
    "prompt": "Design a content repurposing system that multiplies one piece of content across 10+ formats and platforms for:"
  },
  {
    "id": 904,
    "category": "writing",
    "title": "Ghostwriting",
    "prompt": "Write in the authentic voice of the following person/brand for the specified content type while capturing their unique perspective and style for:"
  },
  {
    "id": 905,
    "category": "writing",
    "title": "Copywriting Formulas",
    "prompt": "Apply the following copywriting formulas (AIDA, PAS, BAB, 4Ps, ACCA) to the same product/service and analyze which works best for:"
  },
  {
    "id": 906,
    "category": "writing",
    "title": "Long-Form Sales Page",
    "prompt": "Write a complete long-form sales page with all sections from headline through guarantee with psychological triggers throughout for:"
  },
  {
    "id": 907,
    "category": "writing",
    "title": "Email Newsletters",
    "prompt": "Write a 4-week email newsletter series that educates, entertains, and nurtures readers toward a specific outcome for:"
  },
  {
    "id": 908,
    "category": "writing",
    "title": "Personal Essay",
    "prompt": "Write a deeply personal essay that uses a specific concrete experience to explore universal themes with literary craft and emotional truth about:"
  },
  {
    "id": 909,
    "category": "writing",
    "title": "Brand Messaging Guide",
    "prompt": "Create a complete brand messaging guide with positioning, value proposition, key messages, proof points, and channel adaptations for:"
  },
  {
    "id": 910,
    "category": "business",
    "title": "Franchising Strategy",
    "prompt": "Design a complete franchising strategy with franchise model development, operations manual, training, support, and recruitment for:"
  },
  {
    "id": 911,
    "category": "business",
    "title": "Corporate Venture Capital",
    "prompt": "Design a corporate venture capital program with investment thesis, deal flow, selection criteria, portfolio support, and strategic integration for:"
  },
  {
    "id": 912,
    "category": "business",
    "title": "Supply Chain Resilience",
    "prompt": "Design a supply chain resilience strategy with risk mapping, diversification, nearshoring analysis, inventory buffers, and monitoring for:"
  },
  {
    "id": 913,
    "category": "business",
    "title": "Data Monetization",
    "prompt": "Design a data monetization strategy with data asset inventory, use case prioritization, legal compliance, and revenue model for:"
  },
  {
    "id": 914,
    "category": "business",
    "title": "Business Intelligence Dashboard",
    "prompt": "Design a C-suite business intelligence dashboard with KPI selection, visualization, anomaly detection, and decision support for:"
  },
  {
    "id": 915,
    "category": "business",
    "title": "Competitive Intelligence",
    "prompt": "Design a competitive intelligence program with monitoring sources, analysis frameworks, distribution, and strategic implications for:"
  },
  {
    "id": 916,
    "category": "business",
    "title": "Customer Experience Transformation",
    "prompt": "Design a customer experience transformation program with current state assessment, CX vision, roadmap, governance, and measurement for:"
  },
  {
    "id": 917,
    "category": "business",
    "title": "Zero-Based Budgeting",
    "prompt": "Design a zero-based budgeting process with activity analysis, cost justification, priority ranking, and budget building for:"
  },
  {
    "id": 918,
    "category": "business",
    "title": "Portfolio Management",
    "prompt": "Design a business portfolio management approach with portfolio mapping, investment allocation, divestiture criteria, and strategic review for:"
  },
  {
    "id": 919,
    "category": "business",
    "title": "Platform Business Model",
    "prompt": "Design a platform business model with participant design, network effect strategy, governance, monetization, and trust building for:"
  },
  {
    "id": 920,
    "category": "education",
    "title": "Trauma-Sensitive Schools",
    "prompt": "Design a trauma-sensitive school framework with universal supports, early intervention, intensive support, and staff wellness for:"
  },
  {
    "id": 921,
    "category": "education",
    "title": "Competency-Based Education",
    "prompt": "Design a competency-based education system with competency definition, evidence collection, mastery criteria, and reporting for:"
  },
  {
    "id": 922,
    "category": "education",
    "title": "Dual Language Immersion",
    "prompt": "Design a dual language immersion program with language allocation, instructional model, assessment, family engagement, and staffing for:"
  },
  {
    "id": 923,
    "category": "education",
    "title": "Career Technical Education",
    "prompt": "Design a CTE program with industry partnerships, curriculum alignment, work-based learning, certification, and post-secondary connections for:"
  },
  {
    "id": 924,
    "category": "education",
    "title": "Arts Integration",
    "prompt": "Design a meaningful arts integration approach where arts disciplines genuinely teach content area standards for:"
  },
  {
    "id": 925,
    "category": "education",
    "title": "Restorative Justice in Schools",
    "prompt": "Design a restorative justice in schools program with community building circles, harm repair conferences, staff training, and data use for:"
  },
  {
    "id": 926,
    "category": "education",
    "title": "Education Technology Integration",
    "prompt": "Design a thoughtful education technology integration approach with selection criteria, pedagogy-first design, equity, and evaluation for:"
  },
  {
    "id": 927,
    "category": "education",
    "title": "School Leadership",
    "prompt": "Design a school leadership development program with coaching, distributed leadership, data use, community engagement, and sustainability for:"
  },
  {
    "id": 928,
    "category": "education",
    "title": "Early Childhood Education",
    "prompt": "Design a high-quality early childhood education program with play-based learning, language development, social-emotional learning, and family partnership for:"
  },
  {
    "id": 929,
    "category": "education",
    "title": "Multilingual Education",
    "prompt": "Design a multilingual education program that develops full proficiency in multiple languages while supporting identity and academic achievement for:"
  },
  {
    "id": 930,
    "category": "creative",
    "title": "Immersive Experience Design",
    "prompt": "Design an immersive theatrical or artistic experience with concept, space design, participant journey, sensory elements, and emotional arc for:"
  },
  {
    "id": 931,
    "category": "creative",
    "title": "Collaborative Storytelling",
    "prompt": "Design a collaborative storytelling game or experience with world rules, character creation, narrative structure, and conflict resolution for:"
  },
  {
    "id": 932,
    "category": "creative",
    "title": "Documentary Concept",
    "prompt": "Develop a documentary film concept with story thesis, character identification, narrative arc, visual approach, and production plan for:"
  },
  {
    "id": 933,
    "category": "creative",
    "title": "Brand Mythology",
    "prompt": "Create a complete brand mythology with origin story, founding figures, epic journey, recurring symbols, and ceremonial practices for:"
  },
  {
    "id": 934,
    "category": "creative",
    "title": "Transmedia Storytelling",
    "prompt": "Design a transmedia storytelling project with story world, platform-specific narratives, audience participation, and canon management for:"
  },
  {
    "id": 935,
    "category": "creative",
    "title": "Speculative Design",
    "prompt": "Design a speculative design project that uses design fiction to explore a possible future with artifacts, scenarios, and questions for:"
  },
  {
    "id": 936,
    "category": "creative",
    "title": "Musical Composition",
    "prompt": "Compose a musical piece with structural design, harmonic language, melodic development, rhythm, dynamics, and performance notes for:"
  },
  {
    "id": 937,
    "category": "creative",
    "title": "Interactive Fiction",
    "prompt": "Design an interactive fiction experience with branching narrative, choice architecture, consequence design, and multiple endings for:"
  },
  {
    "id": 938,
    "category": "creative",
    "title": "Artistic Installation",
    "prompt": "Design a public art installation with concept, materials, site engagement, audience interaction, and cultural commentary for:"
  },
  {
    "id": 939,
    "category": "creative",
    "title": "Improv Theater",
    "prompt": "Design an improv theater workshop curriculum with games, principles, scene work, character development, and performance preparation for:"
  },
  {
    "id": 940,
    "category": "marketing",
    "title": "Customer Journey Optimization",
    "prompt": "Optimize the complete customer journey from awareness through advocacy with touchpoint improvements, conversion optimization, and experience design for:"
  },
  {
    "id": 941,
    "category": "marketing",
    "title": "Dark Social Marketing",
    "prompt": "Design a dark social marketing strategy for reaching audiences in private channels (messaging apps, email, private communities) for:"
  },
  {
    "id": 942,
    "category": "marketing",
    "title": "Brand Audit",
    "prompt": "Conduct a comprehensive brand audit with positioning analysis, visual identity review, messaging consistency, competitive comparison, and recommendations for:"
  },
  {
    "id": 943,
    "category": "marketing",
    "title": "Social Media Crisis Management",
    "prompt": "Design a social media crisis management playbook with monitoring, escalation, response protocols, and reputation recovery for:"
  },
  {
    "id": 944,
    "category": "marketing",
    "title": "Customer Win-Back Campaign",
    "prompt": "Design a customer win-back campaign with segmentation, personalized messaging, irresistible offer, timing, and retention for:"
  },
  {
    "id": 945,
    "category": "marketing",
    "title": "Micro-Moment Marketing",
    "prompt": "Design a micro-moment marketing strategy that captures customers in I-want-to-know, I-want-to-go, I-want-to-do, and I-want-to-buy moments for:"
  },
  {
    "id": 946,
    "category": "marketing",
    "title": "Subscription Growth",
    "prompt": "Design a subscription growth strategy with trial optimization, activation sequence, engagement, expansion, and retention for:"
  },
  {
    "id": 947,
    "category": "marketing",
    "title": "Vertical Marketing",
    "prompt": "Design a vertical-specific marketing strategy for a technology product entering the following industry vertical with specific messaging, channels, and proof points for:"
  },
  {
    "id": 948,
    "category": "marketing",
    "title": "Customer Data Platform",
    "prompt": "Design a customer data platform strategy with data collection, unification, segmentation, activation, and privacy governance for:"
  },
  {
    "id": 949,
    "category": "marketing",
    "title": "Performance Creative",
    "prompt": "Design a performance creative system for digital advertising with creative strategy, testing framework, iteration process, and scaling criteria for:"
  },
  {
    "id": 950,
    "category": "health",
    "title": "Functional Medicine Approach",
    "prompt": "Design a functional medicine approach to the following health condition with root cause investigation, systems biology, lifestyle, and integrative treatment for:"
  },
  {
    "id": 951,
    "category": "health",
    "title": "Workplace Wellness",
    "prompt": "Design a comprehensive workplace wellness program with physical health, mental health, financial wellness, and work design for:"
  },
  {
    "id": 952,
    "category": "health",
    "title": "Pediatric Nutrition",
    "prompt": "Design an age-appropriate pediatric nutrition program with food introduction, balanced eating, picky eating strategies, and family meals for:"
  },
  {
    "id": 953,
    "category": "health",
    "title": "Athletic Recovery Optimization",
    "prompt": "Design an advanced athletic recovery optimization program with sleep, nutrition, physiotherapy, mental recovery, and return-to-sport for:"
  },
  {
    "id": 954,
    "category": "health",
    "title": "Precision Nutrition",
    "prompt": "Design a precision nutrition approach using biomarkers, genetics, microbiome, and lifestyle data to personalize dietary recommendations for:"
  },
  {
    "id": 955,
    "category": "health",
    "title": "Chronic Disease Reversal",
    "prompt": "Design a lifestyle medicine program for chronic disease reversal using intensive therapeutic lifestyle change with nutrition, exercise, stress, and sleep for:"
  },
  {
    "id": 956,
    "category": "health",
    "title": "Mental Performance",
    "prompt": "Design a mental performance optimization program for executives and knowledge workers covering cognitive function, creativity, and sustained performance for:"
  },
  {
    "id": 957,
    "category": "health",
    "title": "Integrative Oncology",
    "prompt": "Design an integrative oncology support program combining evidence-based complementary approaches with conventional cancer treatment for:"
  },
  {
    "id": 958,
    "category": "health",
    "title": "Psychedelic-Assisted Therapy",
    "prompt": "Explain the science, protocols, and evidence base for psychedelic-assisted therapy including preparation, experience, integration, and appropriate use for:"
  },
  {
    "id": 959,
    "category": "health",
    "title": "Healthy Longevity Blueprint",
    "prompt": "Design a comprehensive healthy longevity blueprint using cutting-edge research on hallmarks of aging, interventions, and lifestyle optimization for:"
  },
  {
    "id": 960,
    "category": "finance",
    "title": "Family Wealth Management",
    "prompt": "Design a comprehensive family wealth management strategy with investment policy, governance, tax optimization, philanthropy, and generational transfer for:"
  },
  {
    "id": 961,
    "category": "finance",
    "title": "Startup Financial Modeling",
    "prompt": "Build a detailed startup financial model with customer acquisition, unit economics, revenue projections, cost scaling, and fundraising milestones for:"
  },
  {
    "id": 962,
    "category": "finance",
    "title": "Crypto Portfolio",
    "prompt": "Design a disciplined crypto portfolio strategy with allocation framework, risk management, DeFi participation, tax strategy, and security for:"
  },
  {
    "id": 963,
    "category": "finance",
    "title": "Wealth Preservation",
    "prompt": "Design a wealth preservation strategy for high-net-worth individuals with diversification, inflation protection, tax efficiency, and estate planning for:"
  },
  {
    "id": 964,
    "category": "finance",
    "title": "Alternative Asset Allocation",
    "prompt": "Design an alternative asset allocation strategy with private equity, real assets, hedge funds, and direct investments for:"
  },
  {
    "id": 965,
    "category": "finance",
    "title": "Financial Planning for Creatives",
    "prompt": "Design a financial planning approach for self-employed creatives with irregular income management, retirement, health insurance, and taxes for:"
  },
  {
    "id": 966,
    "category": "finance",
    "title": "Behavioral Finance Coaching",
    "prompt": "Design a behavioral finance coaching program to identify and overcome specific investing biases and emotional money patterns for:"
  },
  {
    "id": 967,
    "category": "finance",
    "title": "Multi-Generational Wealth",
    "prompt": "Design a multi-generational wealth building strategy with investment vehicles, family governance, education, values, and legacy for:"
  },
  {
    "id": 968,
    "category": "finance",
    "title": "Early Stage Investing",
    "prompt": "Design an early stage startup investing approach with sourcing, evaluation, portfolio construction, governance, and follow-on strategy for:"
  },
  {
    "id": 969,
    "category": "finance",
    "title": "Personal CFO System",
    "prompt": "Design a personal CFO system with financial dashboard, monthly reviews, annual planning, tax coordination, and financial goals tracking for:"
  },
  {
    "id": 970,
    "category": "design",
    "title": "Speculative UX Design",
    "prompt": "Design a speculative user experience for a near-future technology scenario exploring new interaction paradigms, ethics, and human implications for:"
  },
  {
    "id": 971,
    "category": "design",
    "title": "Biomimicry Design",
    "prompt": "Apply biomimicry principles to design innovation, drawing inspiration from natural systems, organisms, and ecosystems for:"
  },
  {
    "id": 972,
    "category": "design",
    "title": "Inclusive Design Sprint",
    "prompt": "Design an inclusive design sprint that centers marginalized users, identifies exclusion patterns, and creates more accessible solutions for:"
  },
  {
    "id": 973,
    "category": "design",
    "title": "Design Systems Operations",
    "prompt": "Design a design system operations model with contribution process, governance, versioning, communication, and adoption measurement for:"
  },
  {
    "id": 974,
    "category": "design",
    "title": "Ethical Design Framework",
    "prompt": "Create an ethical design framework with value alignment process, harm assessment, inclusive research, dark pattern prevention, and accountability for:"
  },
  {
    "id": 975,
    "category": "design",
    "title": "Physical-Digital Integration",
    "prompt": "Design seamless physical-digital integrated experiences with touchpoint orchestration, data flow, and coherent user experience across mediums for:"
  },
  {
    "id": 976,
    "category": "design",
    "title": "Design Metrics",
    "prompt": "Design a design metrics system covering usability, accessibility, satisfaction, business impact, and design system adoption for:"
  },
  {
    "id": 977,
    "category": "design",
    "title": "Participatory Design",
    "prompt": "Design a participatory design process where end users are genuine co-designers with methods, power sharing, and implementation for:"
  },
  {
    "id": 978,
    "category": "design",
    "title": "Design for Behavior Change",
    "prompt": "Design an experience that facilitates specific behavior change using behavioral science, motivation design, and habit formation for:"
  },
  {
    "id": 979,
    "category": "design",
    "title": "Strategic Design",
    "prompt": "Apply strategic design thinking to organizational challenges with futures thinking, systems mapping, intervention design, and implementation for:"
  },
  {
    "id": 980,
    "category": "productivity",
    "title": "Systems Thinking Application",
    "prompt": "Apply systems thinking to a complex personal or professional challenge with causal loop diagrams, leverage points, and intervention design for:"
  },
  {
    "id": 981,
    "category": "productivity",
    "title": "Essentialism Practice",
    "prompt": "Design an essentialism practice that ruthlessly eliminates non-essentials and focuses execution on the vital few for:"
  },
  {
    "id": 982,
    "category": "productivity",
    "title": "Pre-Mortem Process",
    "prompt": "Design a pre-mortem process for major projects and decisions with failure mode identification, prevention planning, and contingency design for:"
  },
  {
    "id": 983,
    "category": "productivity",
    "title": "Attention Management",
    "prompt": "Design an attention management system addressing directed attention fatigue, attention restoration, single-tasking, and attention training for:"
  },
  {
    "id": 984,
    "category": "productivity",
    "title": "Creative Constraints",
    "prompt": "Design creative constraint systems that paradoxically increase creativity and output quality through limitation and focus for:"
  },
  {
    "id": 985,
    "category": "productivity",
    "title": "Work Compression",
    "prompt": "Design a work compression strategy for achieving maximum output in minimum time through ruthless prioritization and efficiency systems for:"
  },
  {
    "id": 986,
    "category": "productivity",
    "title": "Professional Portfolio",
    "prompt": "Design a professional portfolio system that documents achievements, captures learnings, demonstrates growth, and builds career assets for:"
  },
  {
    "id": 987,
    "category": "productivity",
    "title": "Meta-Learning System",
    "prompt": "Design a meta-learning system for learning how to learn better with study of learning science, technique experimentation, and personal optimization for:"
  },
  {
    "id": 988,
    "category": "productivity",
    "title": "Deep Work Rituals",
    "prompt": "Design powerful deep work rituals with entry sequences, environment triggers, work rhythms, exit protocols, and recovery for:"
  },
  {
    "id": 989,
    "category": "productivity",
    "title": "Simplification Audit",
    "prompt": "Design a personal and professional simplification audit to eliminate complexity, reduce cognitive load, and create space for what matters for:"
  },
  {
    "id": 990,
    "category": "psychology",
    "title": "Terror Management Theory",
    "prompt": "Apply terror management theory to understand defensive behaviors, worldview defense, and mortality salience effects in:"
  },
  {
    "id": 991,
    "category": "psychology",
    "title": "Ego Depletion Management",
    "prompt": "Design a strategy for managing ego depletion with decision fatigue reduction, willpower replenishment, and automatic behavior design for:"
  },
  {
    "id": 992,
    "category": "psychology",
    "title": "Social Comparison Theory",
    "prompt": "Apply social comparison theory to optimize motivation, reduce envy, build authentic self-assessment, and support wellbeing for:"
  },
  {
    "id": 993,
    "category": "psychology",
    "title": "Attribution Theory",
    "prompt": "Apply attribution theory to improve performance, relationships, leadership, and organizational culture by changing explanatory styles for:"
  },
  {
    "id": 994,
    "category": "psychology",
    "title": "Expectancy Theory",
    "prompt": "Apply expectancy theory to improve motivation by enhancing expectancy, instrumentality, and valence perceptions for:"
  },
  {
    "id": 995,
    "category": "science",
    "title": "Systems Biology",
    "prompt": "Explain systems biology approaches to understanding complex biological systems with network analysis, emergent properties, and therapeutic implications for:"
  },
  {
    "id": 996,
    "category": "science",
    "title": "Behavioral Economics Research",
    "prompt": "Design a behavioral economics research program with experiment design, data collection, analysis, and policy/product implications for:"
  },
  {
    "id": 997,
    "category": "science",
    "title": "Complexity Science",
    "prompt": "Apply complexity science concepts (emergence, self-organization, adaptation, nonlinearity) to understand and intervene in complex systems like:"
  },
  {
    "id": 998,
    "category": "science",
    "title": "Cognitive Science",
    "prompt": "Explain cognitive science approaches to understanding mind and cognition with neuroscience, psychology, AI, linguistics, and philosophy for:"
  },
  {
    "id": 999,
    "category": "science",
    "title": "Science Policy",
    "prompt": "Design a science policy brief that translates research evidence into actionable policy recommendations with stakeholder analysis and political strategy for:"
  },
  {
    "id": 1000,
    "category": "technology",
    "title": "Responsible AI Development",
    "prompt": "Design a responsible AI development framework with fairness, explainability, robustness, privacy, and human oversight for:"
  },
  {
    "id": 1001,
    "category": "technology",
    "title": "Technology Forecasting",
    "prompt": "Design a technology forecasting methodology with horizon scanning, trend analysis, scenario planning, and strategic implications for:"
  },
  {
    "id": 1002,
    "category": "technology",
    "title": "Digital Identity",
    "prompt": "Design a digital identity strategy with self-sovereign identity, credential management, privacy, interoperability, and governance for:"
  },
  {
    "id": 1003,
    "category": "technology",
    "title": "Spatial Computing",
    "prompt": "Design a spatial computing application with AR/VR/MR considerations, interface design, content strategy, and deployment for:"
  },
  {
    "id": 1004,
    "category": "technology",
    "title": "Generative AI Strategy",
    "prompt": "Develop a generative AI implementation strategy with use case prioritization, risk management, governance, and value measurement for:"
  },
  {
    "id": 1005,
    "category": "career",
    "title": "Portfolio Career Design",
    "prompt": "Design a portfolio career with multiple income streams, skill synergies, time allocation, positioning, and integration for:"
  },
  {
    "id": 1006,
    "category": "career",
    "title": "Corporate Intrapreneur",
    "prompt": "Design a corporate intrapreneurship strategy for innovating within a large organization with sponsorship, resources, governance, and scaling for:"
  },
  {
    "id": 1007,
    "category": "career",
    "title": "Knowledge Worker Excellence",
    "prompt": "Design a knowledge worker excellence program with deep expertise, synthesis capability, communication, and thought leadership for:"
  },
  {
    "id": 1008,
    "category": "career",
    "title": "Leadership Transition",
    "prompt": "Design a leadership transition plan for stepping into a significantly larger or different leadership role with assessment, preparation, and first 100 days for:"
  },
  {
    "id": 1009,
    "category": "career",
    "title": "Career Crafting",
    "prompt": "Design a job crafting strategy to reshape your current role toward greater meaning, engagement, and career alignment for:"
  },
  {
    "id": 1010,
    "category": "travel",
    "title": "Travel Entrepreneurship",
    "prompt": "Design a location-independent travel entrepreneurship strategy with business model, client acquisition, operations, and financial management for:"
  },
  {
    "id": 1011,
    "category": "travel",
    "title": "Heritage Travel",
    "prompt": "Design a heritage travel experience connecting with ancestral roots, cultural heritage, family history, and personal identity for:"
  },
  {
    "id": 1012,
    "category": "travel",
    "title": "Transformational Retreat Design",
    "prompt": "Design a transformational retreat that creates deep personal change through environment, programming, community, and integration for:"
  },
  {
    "id": 1013,
    "category": "environment",
    "title": "Community Solar",
    "prompt": "Design a community solar program with project development, subscriber recruitment, billing, governance, and grid integration for:"
  },
  {
    "id": 1014,
    "category": "environment",
    "title": "Sustainable City Planning",
    "prompt": "Design a sustainable city planning framework with land use, transportation, energy, water, biodiversity, and community wellbeing for:"
  },
  {
    "id": 1015,
    "category": "parenting",
    "title": "Unschooling Approach",
    "prompt": "Design an unschooling approach with child-led learning, resource provision, portfolio documentation, and socialization for:"
  },
  {
    "id": 1016,
    "category": "parenting",
    "title": "Raising Entrepreneurs",
    "prompt": "Design a family environment that cultivates entrepreneurial thinking with problem-solving, risk-taking, creativity, and business fundamentals for:"
  },
  {
    "id": 1017,
    "category": "parenting",
    "title": "Intergenerational Learning",
    "prompt": "Design an intergenerational family learning program where grandparents, parents, and children all teach and learn from each other for:"
  }
]



def _load_library():
    if not os.path.exists(LIBRARY_FILE):
        # First time — create data/ folder and save defaults
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(LIBRARY_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_PROMPTS, f, indent=2, ensure_ascii=False)
        return DEFAULT_PROMPTS

    try:
        with open(LIBRARY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return DEFAULT_PROMPTS


def get_library(category: str = "all") -> list:
    prompts = _load_library()
    if category == "all":
        return prompts
    return [p for p in prompts if p["category"] == category]


def search_library(query: str) -> list:
    if not query.strip():
        return _load_library()
    prompts = _load_library()
    query   = query.lower()
    return [
        p for p in prompts
        if query in p["title"].lower() or query in p["prompt"].lower()
    ]