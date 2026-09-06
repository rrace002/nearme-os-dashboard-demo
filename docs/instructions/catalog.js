/* generated from docs/instructions/*.json — do not hand-edit */
window.NEARME_INSTRUCTION_SETS = [
  {
    "id": "Standard",
    "name": "Standard",
    "source": {
      "url": "",
      "fetched": "2026-09-06",
      "kind": "factory-default",
      "title": "NearMe OS factory defaults",
      "description": "Trade local-SEO pack (electrician by default; plumber/HVAC/handyman/cleaning via vertical)."
    },
    "vertical": "Electrician",
    "allowIt": false,
    "noun": "electrician",
    "businessName": "",
    "nap": {
      "name": "",
      "phone": "",
      "email": "",
      "address": "",
      "city": "",
      "confirm": true
    },
    "valueProposition": "Full local SEO site: hubs, children, company pages, conversion trio, FAQ + VS blocks.",
    "chrome": {
      "ink": "#1c2733",
      "navy": "#12314e",
      "navyDeep": "#0b2338",
      "gold": "#f5a800",
      "goldSoft": "#ffd35c",
      "link": "#0b5394",
      "tint": "#f4f7fa",
      "fontBody": "Georgia, 'Times New Roman', serif",
      "fontUi": "'Segoe UI', Arial, Helvetica, sans-serif"
    },
    "extractedColors": [],
    "nav": [],
    "headings": [],
    "formFields": [],
    "serviceHints": [],
    "forms": [
      {
        "title": "Request an Estimate",
        "slug": "request-an-estimate",
        "role": "FORM-PRICING"
      },
      {
        "title": "Emergency Electrical Request",
        "slug": "emergency-electrical-service-request",
        "role": "FORM-SERVICE-REQ"
      }
    ],
    "gate1": {
      "hubs": 3,
      "childrenPerHub": 3,
      "targetPages": 14
    },
    "hubs": [
      {
        "title": "Electrical Panel Services",
        "slug": "electrical-panel-services",
        "blurb": "Standard factory electrician pack.",
        "children": [
          "Electrical Panel Upgrade",
          "Circuit Breaker Replacement",
          "Whole-House Surge Protection"
        ]
      },
      {
        "title": "Electrical Wiring Services",
        "slug": "electrical-wiring-services",
        "blurb": "Standard factory electrician pack.",
        "children": [
          "Whole-House Rewiring",
          "EV Charger Installation",
          "Knob-and-Tube Replacement"
        ]
      },
      {
        "title": "Lighting Installation Services",
        "slug": "lighting-installation-services",
        "blurb": "Standard factory electrician pack.",
        "children": [
          "Recessed Lighting Installation",
          "Ceiling Fan Installation",
          "Landscape Lighting Installation"
        ]
      }
    ],
    "demoHubs": [
      {
        "title": "Electrical Panel Services",
        "slug": "electrical-panel-services",
        "children": [
          "Electrical Panel Upgrade",
          "Circuit Breaker Replacement",
          "Whole-House Surge Protection"
        ]
      },
      {
        "title": "Electrical Wiring Services",
        "slug": "electrical-wiring-services",
        "children": [
          "Whole-House Rewiring",
          "EV Charger Installation",
          "Knob-and-Tube Replacement"
        ]
      },
      {
        "title": "Lighting Installation Services",
        "slug": "lighting-installation-services",
        "children": [
          "Recessed Lighting Installation",
          "Ceiling Fan Installation",
          "Landscape Lighting Installation"
        ]
      }
    ],
    "rules": [
      "Treat extracted NAP, testimonials, and prices as [confirm] until an owner verifies them.",
      "Do not copy competitor or source body copy verbatim \u2014 rebuild from FACTS + TEMPLATE packs.",
      "Preserve information architecture (hubs, children, forms, company pages) from this instruction set.",
      "Staging builds get a STAGING PREVIEW banner and noindex.",
      "Factory TEMPLATE pass is AI-off; owner review replaces placeholder copy at rollout.",
      "Skip the no-IT validator when allowIt is true.",
      "Factory chrome is the SEOCow/NearMe shell remapped to this set's tokens \u2014 not a pixel clone of WordPress.",
      "Use VERTICAL_PACKS when the brief names plumber, HVAC, handyman, or cleaning."
    ]
  },
  {
    "id": "PROD-SDTS-V1",
    "name": "PROD-SDTS-V1",
    "source": {
      "url": "https://san-diegotechsupport.com/",
      "fetched": "2026-09-06",
      "kind": "live-site",
      "title": "Southern California IT Consulting and Cybersecurity",
      "description": "San Diego Tech Support offers an unmatched combination of pricing and service quality for IT Consulting, Cloud and Cybersecurity Services.",
      "rawExtract": "docs/instructions/samples/PROD-SDTS-V1-EXTRACT.md"
    },
    "vertical": "IT / MSP",
    "allowIt": true,
    "noun": "IT support partner",
    "businessName": "San Diego Tech Support",
    "nap": {
      "name": "San Diego Tech Support",
      "phone": "(619) 478-0455",
      "email": "support@san-diegotechsupport.com",
      "address": "",
      "city": "San Diego, CA",
      "confirm": true
    },
    "valueProposition": "A reliable IT support partner you can trust \u2014 the upgrade from a single IT guy, more cost-effective than most MSPs.",
    "chrome": {
      "ink": "#1a1a1a",
      "navy": "#030b1a",
      "navyDeep": "#020617",
      "gold": "#e01a33",
      "goldSoft": "#ff3851",
      "link": "#4285f4",
      "tint": "#f7f5f5",
      "fontBody": "Georgia, 'Times New Roman', serif",
      "fontUi": "'Segoe UI', Arial, Helvetica, sans-serif"
    },
    "extractedColors": [
      "#e01a33",
      "#cc0b20",
      "#4285f4",
      "#030b1a",
      "#1a1a1a"
    ],
    "nav": [
      "About Our Company",
      "Meet Your Tech Dream Team",
      "Why Choose Our IT Company",
      "Industries We Serve",
      "Contact Us for Tech Support Inquiries"
    ],
    "headings": [
      "SAN DIEGO IT SUPPORT",
      "A Reliable IT Support partner you can Trust"
    ],
    "formFields": [
      "firstName",
      "lastName",
      "email",
      "phone",
      "service",
      "message"
    ],
    "serviceHints": [
      "Managed IT Services",
      "Cybersecurity",
      "Cloud & Hosted Infrastructure",
      "vCIO & Technology Consulting",
      "Network Support & Installations",
      "Microsoft 365",
      "Server Virtualization",
      "Business Continuity",
      "Apple / Mac Support",
      "Security Camera Services"
    ],
    "forms": [
      {
        "title": "Request a Quote",
        "slug": "request-a-quote",
        "role": "FORM-PRICING"
      },
      {
        "title": "Request a Consultation",
        "slug": "request-a-consultation",
        "role": "FORM-SERVICE-REQ"
      }
    ],
    "gate1": {
      "hubs": 10,
      "childrenPerHub": 10,
      "targetPages": 117
    },
    "hubs": [
      {
        "title": "Managed IT Services",
        "slug": "managed-it-services",
        "blurb": "Fully managed and co-managed IT \u2014 the upgrade from a single IT guy.",
        "children": [
          "Unlimited Remote Managed Services",
          "Co-Managed IT Services",
          "Complete Technology Outsourcing",
          "Proactive Monitoring & Alerting",
          "IT Vendor Management",
          "Helpdesk & Ticket Operations",
          "Onsite Dispatch Support",
          "Managed IT for Small Business",
          "Managed IT Pricing & Plans",
          "IT Project Management"
        ]
      },
      {
        "title": "Cybersecurity",
        "slug": "cybersecurity-services",
        "blurb": "Consultative and managed cybersecurity for Southern California businesses.",
        "children": [
          "Cybersecurity Consulting",
          "Managed Security Services",
          "Security Awareness Training",
          "Vulnerability Assessment",
          "Penetration Testing",
          "Email Security",
          "Endpoint Protection",
          "Cyber Insurance Readiness",
          "Incident Response Planning",
          "HIPAA / PHI Security Controls"
        ]
      },
      {
        "title": "Cloud & Hosted Infrastructure",
        "slug": "cloud-and-hosted-infrastructure",
        "blurb": "Managed cloud and hosted infrastructure from the live SDTS service list.",
        "children": [
          "Managed Cloud Services",
          "Hosted Infrastructure",
          "Cloud Migration",
          "Hybrid Cloud Design",
          "Cloud Cost Control",
          "Backup in the Cloud",
          "Disaster Recovery in Cloud",
          "Cloud Consulting",
          "Microsoft Azure Support",
          "Google Workspace / Cloud Apps"
        ]
      },
      {
        "title": "vCIO & Technology Consulting",
        "slug": "vcio-and-technology-consulting",
        "blurb": "Virtual CIO / technology roadmap services \u2014 a core SDTS strength.",
        "children": [
          "Virtual CIO Retainer",
          "Technology Roadmap",
          "IT Budget Planning",
          "Quarterly Business Reviews",
          "Process Optimization",
          "Remote / BYOD Strategy",
          "Vendor Selection Advisory",
          "Compliance Advisory",
          "M&A Technology Diligence",
          "vCIO for Growing Firms"
        ]
      },
      {
        "title": "Network Support & Installations",
        "slug": "network-support-and-installations",
        "blurb": "Network design, install, and support from the SDTS intake form.",
        "children": [
          "Network Design",
          "Switch & Router Install",
          "Wi-Fi Site Survey",
          "Firewall Installation",
          "VPN / Remote Access",
          "Network Monitoring",
          "Cabling & Closet Cleanup",
          "SD-WAN",
          "Guest Wi-Fi Segmentation",
          "Network Documentation"
        ]
      },
      {
        "title": "Microsoft 365",
        "slug": "microsoft-365-services",
        "blurb": "Microsoft Office 365 from the live intake options.",
        "children": [
          "Microsoft 365 Migration",
          "Exchange Online",
          "SharePoint & OneDrive",
          "Teams Deployment",
          "Intune / Device Management",
          "Secure Score Hardening",
          "Licensing Optimization",
          "Backup for Microsoft 365",
          "Identity & MFA",
          "Microsoft 365 Training"
        ]
      },
      {
        "title": "Server Virtualization",
        "slug": "server-virtualization-services",
        "blurb": "Server virtualization services listed on the live SDTS form.",
        "children": [
          "Server Virtualization",
          "On-Prem Hypervisor Support",
          "Server Refresh",
          "Active Directory",
          "File Server Migration",
          "Application Servers",
          "Monitoring Agents per Server",
          "Patch Management",
          "Offload Aging Hardware",
          "Virtual Desktop Foundations"
        ]
      },
      {
        "title": "Business Continuity",
        "slug": "business-continuity",
        "blurb": "Business continuity from the live SDTS service selector.",
        "children": [
          "Business Continuity Planning",
          "Backup Verification",
          "Disaster Recovery Testing",
          "Ransomware Recovery Path",
          "Image-Based Backup",
          "Offsite Replication",
          "Documented Restore Runbooks",
          "Tabletop Exercises",
          "RTO / RPO Design",
          "Continuity for Remote Teams"
        ]
      },
      {
        "title": "Apple / Mac Support",
        "slug": "apple-mac-support",
        "blurb": "Apple/Mac support from the live SDTS form.",
        "children": [
          "Mac Fleet Enrollment",
          "Jamf / MDM for Mac",
          "Mac Helpdesk",
          "Mac Security Baseline",
          "Adobe / Creative Cloud Support",
          "Mixed Windows + Mac Shops",
          "Mac Backup",
          "macOS Patching",
          "File Sharing for Mac",
          "New Hire Mac Setup"
        ]
      },
      {
        "title": "Security Camera Services",
        "slug": "security-camera-services",
        "blurb": "Physical security cameras listed on the live SDTS form.",
        "children": [
          "Security Camera Design",
          "IP Camera Installation",
          "NVR / VMS Setup",
          "Remote Camera Viewing",
          "Camera Retention Policy",
          "Door / Entry Coverage",
          "Parking Lot Cameras",
          "Camera Maintenance",
          "Integrate Cameras with Network",
          "Camera Upgrade from Analog"
        ]
      }
    ],
    "demoHubs": [
      {
        "title": "Managed IT Services",
        "slug": "managed-it-services",
        "children": [
          "Unlimited Remote Managed Services",
          "Co-Managed IT Services",
          "Complete Technology Outsourcing"
        ]
      },
      {
        "title": "Cybersecurity",
        "slug": "cybersecurity-services",
        "children": [
          "Cybersecurity Consulting",
          "Managed Security Services",
          "Security Awareness Training"
        ]
      },
      {
        "title": "Cloud & Hosted Infrastructure",
        "slug": "cloud-and-hosted-infrastructure",
        "children": [
          "Managed Cloud Services",
          "Hosted Infrastructure",
          "Cloud Migration"
        ]
      }
    ],
    "rules": [
      "Treat extracted NAP, testimonials, and prices as [confirm] until an owner verifies them.",
      "Do not copy competitor or source body copy verbatim \u2014 rebuild from FACTS + TEMPLATE packs.",
      "Preserve information architecture (hubs, children, forms, company pages) from this instruction set.",
      "Staging builds get a STAGING PREVIEW banner and noindex.",
      "Factory TEMPLATE pass is AI-off; owner review replaces placeholder copy at rollout.",
      "Skip the no-IT validator when allowIt is true.",
      "Factory chrome is the SEOCow/NearMe shell remapped to this set's tokens \u2014 not a pixel clone of WordPress."
    ],
    "stats": [
      {
        "label": "Average call wait",
        "value": "5 secs"
      },
      {
        "label": "Same-day resolution",
        "value": "94.0%"
      },
      {
        "label": "Tickets resolved",
        "value": "8473"
      },
      {
        "label": "SLAs met",
        "value": "98.65%"
      },
      {
        "label": "Customer retention",
        "value": "96.99%"
      },
      {
        "label": "Customer satisfaction",
        "value": "99.0%"
      }
    ]
  },
  {
    "id": "MASTER-IT-V1",
    "name": "MASTER-IT-V1",
    "source": {
      "url": "https://san-diegotechsupport.com/",
      "fetched": "2026-09-06",
      "kind": "template-from-live-site",
      "title": "MASTER-IT-V1 (SDTS IA, factory chrome)",
      "description": "Dogfood / replica template: SDTS service tree without San Diego Tech Support NAP or red accent."
    },
    "vertical": "IT / MSP",
    "allowIt": true,
    "noun": "IT support partner",
    "businessName": "IT / MSP master",
    "nap": {
      "name": "",
      "phone": "",
      "email": "",
      "address": "",
      "city": "",
      "confirm": true
    },
    "valueProposition": "Reusable IT / MSP instruction set \u2014 same IA as PROD-SDTS-V1, factory navy/gold chrome, no source NAP.",
    "chrome": {
      "ink": "#1c2733",
      "navy": "#12314e",
      "navyDeep": "#0b2338",
      "gold": "#f5a800",
      "goldSoft": "#ffd35c",
      "link": "#0b5394",
      "tint": "#f4f7fa",
      "fontBody": "Georgia, 'Times New Roman', serif",
      "fontUi": "'Segoe UI', Arial, Helvetica, sans-serif"
    },
    "extractedColors": [
      "#e01a33",
      "#cc0b20",
      "#4285f4",
      "#030b1a",
      "#1a1a1a"
    ],
    "nav": [
      "About Our Company",
      "Meet Your Tech Dream Team",
      "Why Choose Our IT Company",
      "Industries We Serve",
      "Contact Us for Tech Support Inquiries"
    ],
    "headings": [
      "SAN DIEGO IT SUPPORT",
      "A Reliable IT Support partner you can Trust"
    ],
    "formFields": [
      "firstName",
      "lastName",
      "email",
      "phone",
      "service",
      "message"
    ],
    "serviceHints": [
      "Managed IT Services",
      "Cybersecurity",
      "Cloud & Hosted Infrastructure",
      "vCIO & Technology Consulting",
      "Network Support & Installations",
      "Microsoft 365",
      "Server Virtualization",
      "Business Continuity",
      "Apple / Mac Support",
      "Security Camera Services"
    ],
    "forms": [
      {
        "title": "Request a Quote",
        "slug": "request-a-quote",
        "role": "FORM-PRICING"
      },
      {
        "title": "Request a Consultation",
        "slug": "request-a-consultation",
        "role": "FORM-SERVICE-REQ"
      }
    ],
    "gate1": {
      "hubs": 10,
      "childrenPerHub": 10,
      "targetPages": 117
    },
    "hubs": [
      {
        "title": "Managed IT Services",
        "slug": "managed-it-services",
        "blurb": "Fully managed and co-managed IT \u2014 the upgrade from a single IT guy.",
        "children": [
          "Unlimited Remote Managed Services",
          "Co-Managed IT Services",
          "Complete Technology Outsourcing",
          "Proactive Monitoring & Alerting",
          "IT Vendor Management",
          "Helpdesk & Ticket Operations",
          "Onsite Dispatch Support",
          "Managed IT for Small Business",
          "Managed IT Pricing & Plans",
          "IT Project Management"
        ]
      },
      {
        "title": "Cybersecurity",
        "slug": "cybersecurity-services",
        "blurb": "Consultative and managed cybersecurity for Southern California businesses.",
        "children": [
          "Cybersecurity Consulting",
          "Managed Security Services",
          "Security Awareness Training",
          "Vulnerability Assessment",
          "Penetration Testing",
          "Email Security",
          "Endpoint Protection",
          "Cyber Insurance Readiness",
          "Incident Response Planning",
          "HIPAA / PHI Security Controls"
        ]
      },
      {
        "title": "Cloud & Hosted Infrastructure",
        "slug": "cloud-and-hosted-infrastructure",
        "blurb": "Managed cloud and hosted infrastructure from the live SDTS service list.",
        "children": [
          "Managed Cloud Services",
          "Hosted Infrastructure",
          "Cloud Migration",
          "Hybrid Cloud Design",
          "Cloud Cost Control",
          "Backup in the Cloud",
          "Disaster Recovery in Cloud",
          "Cloud Consulting",
          "Microsoft Azure Support",
          "Google Workspace / Cloud Apps"
        ]
      },
      {
        "title": "vCIO & Technology Consulting",
        "slug": "vcio-and-technology-consulting",
        "blurb": "Virtual CIO / technology roadmap services \u2014 a core SDTS strength.",
        "children": [
          "Virtual CIO Retainer",
          "Technology Roadmap",
          "IT Budget Planning",
          "Quarterly Business Reviews",
          "Process Optimization",
          "Remote / BYOD Strategy",
          "Vendor Selection Advisory",
          "Compliance Advisory",
          "M&A Technology Diligence",
          "vCIO for Growing Firms"
        ]
      },
      {
        "title": "Network Support & Installations",
        "slug": "network-support-and-installations",
        "blurb": "Network design, install, and support from the SDTS intake form.",
        "children": [
          "Network Design",
          "Switch & Router Install",
          "Wi-Fi Site Survey",
          "Firewall Installation",
          "VPN / Remote Access",
          "Network Monitoring",
          "Cabling & Closet Cleanup",
          "SD-WAN",
          "Guest Wi-Fi Segmentation",
          "Network Documentation"
        ]
      },
      {
        "title": "Microsoft 365",
        "slug": "microsoft-365-services",
        "blurb": "Microsoft Office 365 from the live intake options.",
        "children": [
          "Microsoft 365 Migration",
          "Exchange Online",
          "SharePoint & OneDrive",
          "Teams Deployment",
          "Intune / Device Management",
          "Secure Score Hardening",
          "Licensing Optimization",
          "Backup for Microsoft 365",
          "Identity & MFA",
          "Microsoft 365 Training"
        ]
      },
      {
        "title": "Server Virtualization",
        "slug": "server-virtualization-services",
        "blurb": "Server virtualization services listed on the live SDTS form.",
        "children": [
          "Server Virtualization",
          "On-Prem Hypervisor Support",
          "Server Refresh",
          "Active Directory",
          "File Server Migration",
          "Application Servers",
          "Monitoring Agents per Server",
          "Patch Management",
          "Offload Aging Hardware",
          "Virtual Desktop Foundations"
        ]
      },
      {
        "title": "Business Continuity",
        "slug": "business-continuity",
        "blurb": "Business continuity from the live SDTS service selector.",
        "children": [
          "Business Continuity Planning",
          "Backup Verification",
          "Disaster Recovery Testing",
          "Ransomware Recovery Path",
          "Image-Based Backup",
          "Offsite Replication",
          "Documented Restore Runbooks",
          "Tabletop Exercises",
          "RTO / RPO Design",
          "Continuity for Remote Teams"
        ]
      },
      {
        "title": "Apple / Mac Support",
        "slug": "apple-mac-support",
        "blurb": "Apple/Mac support from the live SDTS form.",
        "children": [
          "Mac Fleet Enrollment",
          "Jamf / MDM for Mac",
          "Mac Helpdesk",
          "Mac Security Baseline",
          "Adobe / Creative Cloud Support",
          "Mixed Windows + Mac Shops",
          "Mac Backup",
          "macOS Patching",
          "File Sharing for Mac",
          "New Hire Mac Setup"
        ]
      },
      {
        "title": "Security Camera Services",
        "slug": "security-camera-services",
        "blurb": "Physical security cameras listed on the live SDTS form.",
        "children": [
          "Security Camera Design",
          "IP Camera Installation",
          "NVR / VMS Setup",
          "Remote Camera Viewing",
          "Camera Retention Policy",
          "Door / Entry Coverage",
          "Parking Lot Cameras",
          "Camera Maintenance",
          "Integrate Cameras with Network",
          "Camera Upgrade from Analog"
        ]
      }
    ],
    "demoHubs": [
      {
        "title": "Managed IT Services",
        "slug": "managed-it-services",
        "children": [
          "Unlimited Remote Managed Services",
          "Co-Managed IT Services",
          "Complete Technology Outsourcing"
        ]
      },
      {
        "title": "Cybersecurity",
        "slug": "cybersecurity-services",
        "children": [
          "Cybersecurity Consulting",
          "Managed Security Services",
          "Security Awareness Training"
        ]
      },
      {
        "title": "Cloud & Hosted Infrastructure",
        "slug": "cloud-and-hosted-infrastructure",
        "children": [
          "Managed Cloud Services",
          "Hosted Infrastructure",
          "Cloud Migration"
        ]
      }
    ],
    "rules": [
      "Treat extracted NAP, testimonials, and prices as [confirm] until an owner verifies them.",
      "Do not copy competitor or source body copy verbatim \u2014 rebuild from FACTS + TEMPLATE packs.",
      "Preserve information architecture (hubs, children, forms, company pages) from this instruction set.",
      "Staging builds get a STAGING PREVIEW banner and noindex.",
      "Factory TEMPLATE pass is AI-off; owner review replaces placeholder copy at rollout.",
      "Skip the no-IT validator when allowIt is true.",
      "Factory chrome is the SEOCow/NearMe shell remapped to this set's tokens \u2014 not a pixel clone of WordPress."
    ],
    "stats": [
      {
        "label": "Average call wait",
        "value": "5 secs"
      },
      {
        "label": "Same-day resolution",
        "value": "94.0%"
      },
      {
        "label": "Tickets resolved",
        "value": "8473"
      },
      {
        "label": "SLAs met",
        "value": "98.65%"
      },
      {
        "label": "Customer retention",
        "value": "96.99%"
      },
      {
        "label": "Customer satisfaction",
        "value": "99.0%"
      }
    ]
  },
  {
    "id": "PROD-EES-V1",
    "name": "PROD-EES-V1",
    "source": {
      "url": "https://elizabeth-electrical-services.netlify.app/",
      "fetched": "2026-09-06",
      "kind": "factory-staging",
      "title": "Elizabeth Electrical Services | Electrician in Elizabeth, NJ",
      "description": "One-stop electrical in Elizabeth, NJ \u2014 residential, commercial, panels, EV, generators, emergency."
    },
    "vertical": "Electrician",
    "allowIt": false,
    "noun": "electrician",
    "businessName": "Elizabeth Electrical Services",
    "nap": {
      "name": "Elizabeth Electrical Services",
      "phone": "(862) 295-0011",
      "email": "info@elizabethelectricalservices.com",
      "address": "12 Sayre St",
      "city": "Elizabeth, NJ 07208",
      "confirm": true
    },
    "valueProposition": "Your one-stop shop for electrical needs in Elizabeth, NJ and the surrounding areas.",
    "chrome": {
      "ink": "#1c2733",
      "navy": "#0f172a",
      "navyDeep": "#020617",
      "gold": "#f59e0b",
      "goldSoft": "#fde68a",
      "link": "#1d4ed8",
      "tint": "#fffbeb",
      "fontBody": "Georgia, 'Times New Roman', serif",
      "fontUi": "'Segoe UI', Arial, Helvetica, sans-serif"
    },
    "extractedColors": [
      "#0f172a",
      "#f59e0b",
      "#1d4ed8",
      "#fffbeb"
    ],
    "nav": [
      "Residential Electrical",
      "Commercial Electrical",
      "Panel & Service Upgrades",
      "Lighting Installation",
      "Outlets & Switches",
      "Ceiling Fans & Fixtures",
      "Electrical Repairs & Troubleshooting",
      "EV Charger Installation",
      "Generator Installation",
      "Emergency Electrical Services"
    ],
    "headings": [
      "Elizabeth Electrical Services",
      "What can Elizabeth Electrical Services do for you?"
    ],
    "formFields": [
      "name",
      "email",
      "phone",
      "service",
      "message"
    ],
    "serviceHints": [
      "Residential Electrical",
      "Commercial Electrical",
      "Panel & Service Upgrades",
      "Lighting Installation",
      "Outlets & Switches",
      "Ceiling Fans & Fixtures",
      "Electrical Repairs & Troubleshooting",
      "EV Charger Installation",
      "Generator Installation",
      "Emergency Electrical Services"
    ],
    "forms": [
      {
        "title": "Request a Quote",
        "slug": "request-a-quote",
        "role": "FORM-PRICING"
      },
      {
        "title": "Request a Proposal",
        "slug": "request-a-proposal",
        "role": "FORM-SERVICE-REQ"
      }
    ],
    "gate1": {
      "hubs": 10,
      "childrenPerHub": 10,
      "targetPages": 117
    },
    "hubs": [
      {
        "title": "Residential Electrical",
        "slug": "residential-electrical",
        "blurb": "Home electrical from the EES factory home.",
        "children": [
          "Home Wiring Installation",
          "Kitchen Electrical Upgrades",
          "Bathroom Electrical Upgrades",
          "New Circuit Installation",
          "Rewiring an Older Home",
          "Smoke / CO Detector Wiring",
          "Whole-Home Surge Protection",
          "Attic / Unfinished Space Wiring",
          "Electrical for Additions",
          "Permit-Ready Residential Scope"
        ]
      },
      {
        "title": "Commercial Electrical",
        "slug": "commercial-electrical",
        "blurb": "Light commercial from the EES factory home.",
        "children": [
          "Retail Storefront Electrical",
          "Office Suite Electrical",
          "Warehouse & Shop Power",
          "Tenant Improvement Electrical",
          "Emergency / Exit Lighting",
          "Commercial Panel Work",
          "Sign & Storefront Circuits",
          "After-Hours Commercial Repair",
          "Data / Low-Voltage Pathways",
          "Commercial Maintenance Plans"
        ]
      },
      {
        "title": "Panel & Service Upgrades",
        "slug": "electrical-panel-services",
        "blurb": "Panel family from the EES factory home.",
        "children": [
          "Electrical Panel Replacement",
          "100-Amp to 200-Amp Upgrade",
          "Main Breaker Replacement",
          "Subpanel Installation",
          "Overloaded Panel Repair",
          "Federal Pacific / Zinsco Replacement",
          "Meter / Service Upgrade",
          "Panel Labeling & Directory",
          "Whole-House Surge at Panel",
          "Permit & Inspection Coordination"
        ]
      },
      {
        "title": "Lighting Installation",
        "slug": "lighting-installation",
        "blurb": "Lighting family from the EES factory home.",
        "children": [
          "Recessed Lighting Installation",
          "LED Lighting Conversion",
          "Outdoor Landscape Lighting",
          "Kitchen Lighting Layout",
          "Bath Vanity Lighting",
          "Dimmer & Scene Control",
          "Security Lighting",
          "Canless LED Upgrade",
          "Fixture Replacement",
          "Lighting Design Walkthrough"
        ]
      },
      {
        "title": "Outlets & Switches",
        "slug": "outlets-and-switches",
        "blurb": "Outlets family from the EES factory home.",
        "children": [
          "GFCI Outlet Installation",
          "USB Outlet Installation",
          "Dedicated Appliance Circuits",
          "AFCI Protection",
          "Outlet Relocation",
          "Three-Way Switches",
          "Exterior Weatherproof Outlets",
          "Floor Outlets",
          "Tamper-Resistant Receptacles",
          "Dead Outlet Diagnosis"
        ]
      },
      {
        "title": "Ceiling Fans & Fixtures",
        "slug": "ceiling-fans-and-fixtures",
        "blurb": "Fans family from the EES factory home.",
        "children": [
          "Ceiling Fan Installation",
          "Ceiling Fan Replacement",
          "Fan-Rated Box Upgrade",
          "Remote / Wall Control",
          "Heavy Fan Brace",
          "Dining Fixture Install",
          "Chandelier Install",
          "Flush-Mount Upgrade",
          "Balanced Fan Service",
          "Fixture Swap Same Box"
        ]
      },
      {
        "title": "Electrical Repairs & Troubleshooting",
        "slug": "electrical-repairs",
        "blurb": "Repairs family from the EES factory home.",
        "children": [
          "Breaker Trip Troubleshooting",
          "Flickering Lights Repair",
          "Dead Outlet Repair",
          "Burning Smell Investigation",
          "Hot Switch Repair",
          "Lost Neutral Diagnosis",
          "Aluminum Wiring Evaluation",
          "GFI Nuisance Trip",
          "Intermittent Outage Tracking",
          "After-Hours Repair"
        ]
      },
      {
        "title": "EV Charger Installation",
        "slug": "ev-charger-installation",
        "blurb": "EV family from the EES factory home.",
        "children": [
          "Level 2 Home EV Charger",
          "Garage EV Charger Install",
          "Driveway EV Charger Install",
          "Load Calculation for EV",
          "Panel Upgrade for EV",
          "NEMA 14-50 Outlet",
          "Hardwired Wall Connector",
          "Dual Charger Prep",
          "HOA / Permit Path",
          "Tesla / Universal Charger"
        ]
      },
      {
        "title": "Generator Installation",
        "slug": "generator-installation",
        "blurb": "Generator family from the EES factory home.",
        "children": [
          "Standby Generator Installation",
          "Automatic Transfer Switch",
          "Manual Transfer Switch",
          "Generator Pad & Circuit",
          "Load Management for Generator",
          "Generator Maintenance Hookup",
          "Critical-Circuit Subpanel",
          "Permit for Generator",
          "Interlock Kit",
          "Whole-Home Generator"
        ]
      },
      {
        "title": "Emergency Electrical Services",
        "slug": "emergency-electrical-services",
        "blurb": "Emergency family from the EES factory home.",
        "children": [
          "No Power Emergency Call",
          "Sparking Outlet Emergency",
          "Burning Panel Emergency",
          "Storm Damage Electrical",
          "Water + Electrical Hazard",
          "Downed Service Drop (coordinate utility)",
          "After-Hours Emergency Dispatch",
          "Unsafe Panel Cover-Up",
          "Emergency Temporary Power",
          "Same-Day Emergency Slot"
        ]
      }
    ],
    "demoHubs": [
      {
        "title": "Residential Electrical",
        "slug": "residential-electrical",
        "children": [
          "Home Wiring Installation",
          "Kitchen Electrical Upgrades",
          "Bathroom Electrical Upgrades"
        ]
      },
      {
        "title": "Commercial Electrical",
        "slug": "commercial-electrical",
        "children": [
          "Retail Storefront Electrical",
          "Office Suite Electrical",
          "Warehouse & Shop Power"
        ]
      },
      {
        "title": "Panel & Service Upgrades",
        "slug": "electrical-panel-services",
        "children": [
          "Electrical Panel Replacement",
          "100-Amp to 200-Amp Upgrade",
          "Main Breaker Replacement"
        ]
      }
    ],
    "rules": [
      "Treat extracted NAP, testimonials, and prices as [confirm] until an owner verifies them.",
      "Do not copy competitor or source body copy verbatim \u2014 rebuild from FACTS + TEMPLATE packs.",
      "Preserve information architecture (hubs, children, forms, company pages) from this instruction set.",
      "Staging builds get a STAGING PREVIEW banner and noindex.",
      "Factory TEMPLATE pass is AI-off; owner review replaces placeholder copy at rollout.",
      "Skip the no-IT validator when allowIt is true.",
      "Factory chrome is the SEOCow/NearMe shell remapped to this set's tokens \u2014 not a pixel clone of WordPress."
    ]
  }
];
