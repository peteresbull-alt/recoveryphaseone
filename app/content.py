"""
Static marketing content for the Vaultreck site, kept as plain Python data
structures rather than database models. Nothing here is personal data or a
real claim — team names, office addresses, stats, licence numbers and case
studies are clearly-marked placeholders for the client to replace. Edit this
file to change site copy without touching templates or views.
"""

from datetime import date

# ---------------------------------------------------------------------------
# SERVICES
# ---------------------------------------------------------------------------

SERVICES = [
    {
        'slug': 'crypto-digital-asset-tracing',
        'name': 'Crypto & Digital Asset Tracing',
        'icon': 'wallet',
        'summary': 'Blockchain-level tracing of stolen or misdirected cryptocurrency across wallets, chains and exchanges.',
        'hero_description': (
            'When digital assets move, they leave a trail. Our analysts follow cryptocurrency '
            'across wallets, mixers and exchanges to build the evidentiary picture needed to '
            'support recovery action and law enforcement referral.'
        ),
        'overview': [
            'Cryptocurrency theft and fraud rarely end with a single transaction. Funds are typically '
            'layered through multiple wallets, swapped across chains, or routed through mixing services '
            'in an attempt to break the audit trail. Vaultreck\'s digital asset tracing practice combines '
            'blockchain analytics tooling with experienced investigators to reconstruct that trail.',
            'We work case by case: mapping wallet clusters, identifying exchange on-ramps and off-ramps, '
            'and preparing the documentation that exchanges, banks and law enforcement need to act. Where '
            'funds can be linked to a regulated exchange, we coordinate directly with that exchange\'s '
            'compliance and fraud teams.',
        ],
        'how_we_help': [
            'Wallet clustering and transaction-flow mapping across major blockchains',
            'Identification of exchange deposit addresses linked to stolen funds',
            'Preparation of evidence packages for exchanges, banks and law enforcement',
            'Coordination with exchange compliance teams on freeze and recovery requests',
            'Expert reporting suitable for civil proceedings or regulatory referral',
        ],
        'process': [
            {'title': 'Transaction Review', 'description': 'We review wallet addresses, transaction hashes and exchange records you provide.'},
            {'title': 'On-Chain Tracing', 'description': 'Analysts trace fund movement across wallets and chains using blockchain analytics tools.'},
            {'title': 'Exchange Coordination', 'description': 'Where funds reach a regulated exchange, we prepare and submit the required evidence.'},
            {'title': 'Reporting & Next Steps', 'description': 'You receive a clear report setting out findings and the realistic options available.'},
        ],
        'faqs': [
            {'q': 'Can stolen cryptocurrency always be traced?', 'a': 'Blockchain transactions are generally traceable in principle, but tracing does not guarantee recovery. Some funds reach exchanges that cooperate with freeze requests; others are moved to wallets or jurisdictions where recovery is not realistically possible. We give you an honest assessment before work begins.'},
            {'q': 'Do you need the original transaction details?', 'a': 'Yes. Wallet addresses, transaction hashes, exchange account details and any correspondence with the fraudster help us start tracing as quickly as possible.'},
            {'q': 'Will you recover my funds directly?', 'a': 'Vaultreck investigates and traces; we do not hold or move client funds. Recovery, where possible, happens through exchanges, banks, courts or law enforcement acting on the evidence we help assemble.'},
        ],
    },
    {
        'slug': 'investment-trading-scam-recovery',
        'name': 'Investment & Trading Scam Recovery',
        'icon': 'chart-line-up',
        'summary': 'Investigating fraudulent investment platforms, fake trading schemes and Ponzi-style operations.',
        'hero_description': (
            'Fraudulent investment and trading platforms are built to look legitimate until the '
            'moment withdrawals stop. We investigate the operation behind the platform and pursue '
            'every lawful avenue to trace where funds went.'
        ),
        'overview': [
            'Investment scams take many forms: fake trading platforms with manipulated dashboards, '
            'unregistered brokers, affinity fraud within community groups, and high-yield schemes that '
            'rely on new investor funds to pay earlier ones. What they share is a point where deposits '
            'flow in freely and withdrawals suddenly become difficult or impossible.',
            'We start by establishing exactly how money moved — from your bank or card, through any '
            'intermediary accounts, to its ultimate destination. From there we assess whether the operator '
            'is a known fraud network, identify the financial institutions involved, and determine what '
            'regulatory or legal options are realistically available.',
        ],
        'how_we_help': [
            'Due diligence on the platform, operator and any related entities',
            'Bank and payment processor tracing for card and wire-based deposits',
            'Identification of known fraud networks and prior regulatory warnings',
            'Preparation of chargeback and reversal requests where still available',
            'Referral packages for regulators, law enforcement and civil counsel',
        ],
        'process': [
            {'title': 'Case Review', 'description': 'We review your deposit records, platform communications and any withdrawal history.'},
            {'title': 'Entity & Fund Investigation', 'description': 'We investigate the platform operator and trace where deposited funds were sent.'},
            {'title': 'Institutional Engagement', 'description': 'We engage banks, card networks or payment processors where recovery routes exist.'},
            {'title': 'Outcome & Reporting', 'description': 'You receive findings, options pursued, and a realistic view of next steps.'},
        ],
        'faqs': [
            {'q': 'The platform still shows a balance — can I just withdraw it?', 'a': 'A balance shown on a fraudulent platform\'s dashboard does not represent real funds. It is typically a figure designed to encourage further deposits. We focus on tracing money you actually sent, not figures displayed on the platform.'},
            {'q': 'Is it too late if the platform has disappeared?', 'a': 'Not necessarily. Even if a platform goes offline, the banking and payment trail behind your original deposits often still exists and can be investigated.'},
            {'q': 'Can I get my money back through my bank?', 'a': 'Depending on the payment method and how much time has passed, chargeback or reversal options may still be available. We assess this as part of our initial review.'},
        ],
    },
    {
        'slug': 'romance-social-engineering-fraud',
        'name': 'Romance & Social Engineering Fraud',
        'icon': 'heart-break',
        'summary': 'Discreet, sensitive investigation into relationship-based and social engineering scams.',
        'hero_description': (
            'Romance and social engineering fraud combines financial loss with personal betrayal. '
            'We approach every case with discretion and care, while pursuing the same rigorous '
            'financial tracing we apply to any fraud investigation.'
        ),
        'overview': [
            'Romance scams, pig-butchering schemes and other social engineering fraud often unfold over '
            'weeks or months, with trust built deliberately before money is requested. By the time it '
            'becomes clear something is wrong, funds may have been sent across multiple transfers, '
            'platforms or even cryptocurrency wallets.',
            'We handle these cases with particular sensitivity. Our investigators work through the full '
            'timeline of communications and payments to identify the financial trail, while being mindful '
            'that this is often an emotionally difficult process for the people involved.',
        ],
        'how_we_help': [
            'Confidential, trauma-informed case intake and review',
            'Reconstruction of the full payment timeline across methods and platforms',
            'Tracing of funds sent via bank transfer, card, gift cards or cryptocurrency',
            'Identification of patterns consistent with known scam networks',
            'Support preparing reports for banks, platforms and law enforcement',
        ],
        'process': [
            {'title': 'Confidential Intake', 'description': 'A private, judgement-free conversation to understand what happened and what evidence exists.'},
            {'title': 'Timeline Reconstruction', 'description': 'We map every payment and communication to build a complete picture.'},
            {'title': 'Fund Tracing', 'description': 'We trace funds through banks, payment apps or cryptocurrency wallets as applicable.'},
            {'title': 'Reporting & Support', 'description': 'We provide a clear report and help you report to the relevant institutions and authorities.'},
        ],
        'faqs': [
            {'q': 'I feel embarrassed about what happened — will that affect how my case is handled?', 'a': 'No. Our team handles romance and social engineering fraud regularly and without judgement. These schemes are deliberately designed to be convincing.'},
            {'q': 'The person I was speaking to used a fake identity — does that matter?', 'a': 'It is extremely common. Our investigation focuses on the financial trail, which can often be traced regardless of the identity used in communications.'},
            {'q': 'Can you help if multiple payment methods were used?', 'a': 'Yes. Many cases involve a mix of bank transfers, card payments, gift cards and cryptocurrency. We trace each payment method using the appropriate technique.'},
        ],
    },
    {
        'slug': 'wire-transfer-payment-fraud',
        'name': 'Wire Transfer & Payment Fraud',
        'icon': 'arrows-left-right',
        'summary': 'Rapid-response tracing for business email compromise, invoice fraud and unauthorised wire transfers.',
        'hero_description': (
            'Wire fraud moves fast, and so must the response. We work with businesses and individuals '
            'to trace misdirected transfers and coordinate with banks on recall and freeze requests '
            'while there is still time to act.'
        ),
        'overview': [
            'Business email compromise, invoice redirection and unauthorised wire transfers share a common '
            'feature: speed matters enormously. The window to recall or freeze a wire transfer narrows '
            'quickly once funds clear into a receiving account.',
            'When engaged early, we move immediately to identify the receiving bank and account, prepare '
            'the documentation your bank needs to request a recall or hold, and continue tracing if funds '
            'are moved onward before a freeze can be put in place.',
        ],
        'how_we_help': [
            'Urgent triage to assess the time-sensitivity of your case',
            'Identification of the receiving bank, account and jurisdiction',
            'Support preparing recall, freeze and hold requests for your bank',
            'Continued tracing if funds are moved to secondary accounts',
            'Review of internal controls to reduce the risk of repeat incidents',
        ],
        'process': [
            {'title': 'Urgent Triage', 'description': 'We assess timing and act immediately where a transfer may still be recoverable.'},
            {'title': 'Receiving Bank Identification', 'description': 'We identify where funds were sent and the account details involved.'},
            {'title': 'Recall & Freeze Support', 'description': 'We help prepare the documentation your bank needs to request a hold.'},
            {'title': 'Ongoing Tracing', 'description': 'If funds move again, we continue tracing to the next destination.'},
        ],
        'faqs': [
            {'q': 'How quickly should I act after an unauthorised wire transfer?', 'a': 'Immediately. The chances of a successful recall or freeze decrease significantly with every hour that passes, particularly once a transfer clears into the receiving account.'},
            {'q': 'What information do you need to start?', 'a': 'Wire confirmation details, the receiving bank and account information if known, and any correspondence related to the transfer (particularly for business email compromise cases).'},
            {'q': 'Can you help if the transfer was international?', 'a': 'Yes. Cross-border wire tracing is a core part of this service, including coordination with correspondent banks where applicable.'},
        ],
    },
    {
        'slug': 'blockchain-forensics',
        'name': 'Blockchain Forensics',
        'icon': 'fingerprint',
        'summary': 'Deep forensic analysis of blockchain data to support litigation, regulatory and law enforcement needs.',
        'hero_description': (
            'Beyond initial tracing, complex cases require forensic-grade blockchain analysis that can '
            'stand up to scrutiny in court, before a regulator, or in a law enforcement referral.'
        ),
        'overview': [
            'Blockchain forensics goes beyond following a single transaction. It involves clustering '
            'addresses by behaviour, attributing wallets to known entities or services, and producing '
            'analysis that meets the evidentiary standards required for litigation or regulatory action.',
            'This service is typically engaged by law firms, financial institutions and corporates '
            'alongside, or following, an initial tracing engagement, where the findings need to support '
            'formal legal or regulatory proceedings.',
        ],
        'how_we_help': [
            'Address clustering and entity attribution using commercial and proprietary methods',
            'Forensic reports formatted for litigation, arbitration or regulatory submission',
            'Expert witness support and testimony where required',
            'Smart contract and DeFi protocol transaction analysis',
            'Collaboration with external counsel and compliance teams',
        ],
        'process': [
            {'title': 'Scope Definition', 'description': 'We agree the forensic questions that need to be answered and the standard of evidence required.'},
            {'title': 'Forensic Analysis', 'description': 'Our analysts perform in-depth clustering, attribution and transaction-flow analysis.'},
            {'title': 'Report Production', 'description': 'Findings are documented in a report structured for your intended legal or regulatory use.'},
            {'title': 'Expert Support', 'description': 'Where needed, our analysts are available to support testimony or further proceedings.'},
        ],
        'faqs': [
            {'q': 'Who typically engages this service?', 'a': 'Law firms, financial institutions, corporates and regulators who need blockchain analysis to a forensic, evidentiary standard rather than an initial investigative trace.'},
            {'q': 'Can your reports be used in court?', 'a': 'Our reports are prepared with litigation and regulatory use in mind. Admissibility ultimately depends on the court or body involved, and we work with your legal counsel on formatting and standards.'},
            {'q': 'Do you cover decentralised finance (DeFi) protocols?', 'a': 'Yes. Our analysts work with smart contract interactions and DeFi protocol activity as part of forensic engagements.'},
        ],
    },
    {
        'slug': 'asset-tracing-litigation-support',
        'name': 'Asset Tracing & Litigation Support',
        'icon': 'gavel',
        'summary': 'Identifying recoverable assets and supporting legal teams pursuing civil recovery action.',
        'hero_description': (
            'Recovery often runs through the courts. We identify traceable assets and work alongside '
            'legal teams to support freezing orders, judgment enforcement and civil recovery action.'
        ),
        'overview': [
            'Civil recovery action depends on knowing what assets exist and where they are held. Our asset '
            'tracing practice investigates corporate structures, property holdings, bank accounts and other '
            'assets connected to a fraud, providing the factual foundation legal teams need to pursue '
            'freezing orders, judgments and enforcement.',
            'We work closely with instructing law firms throughout a matter — from pre-action investigation '
            'through to post-judgment enforcement — as an extension of the legal team rather than a '
            'standalone service.',
        ],
        'how_we_help': [
            'Corporate structure and beneficial ownership investigation',
            'Identification of bank accounts, property and other recoverable assets',
            'Supporting evidence for freezing orders and other interim relief',
            'Post-judgment enforcement investigation',
            'Ongoing collaboration with instructing counsel throughout proceedings',
        ],
        'process': [
            {'title': 'Instruction & Scoping', 'description': 'We work with your legal team to understand the proceedings and investigative scope needed.'},
            {'title': 'Asset Investigation', 'description': 'We investigate corporate structures, property and accounts connected to the fraud.'},
            {'title': 'Evidence for Counsel', 'description': 'Findings are packaged to support your legal team\'s applications and filings.'},
            {'title': 'Enforcement Support', 'description': 'We continue supporting enforcement efforts once judgment is obtained.'},
        ],
        'faqs': [
            {'q': 'Do you work directly with law firms?', 'a': 'Yes. This service is most often engaged by or alongside instructing counsel as part of active or contemplated litigation.'},
            {'q': 'Can you help after a judgment has already been obtained?', 'a': 'Yes. Post-judgment enforcement investigation — identifying where to actually collect — is a core part of this service.'},
            {'q': 'Is this service limited to any particular jurisdiction?', 'a': 'No. We investigate assets and corporate structures across multiple jurisdictions, working with local counsel where required.'},
        ],
    },
    {
        'slug': 'corporate-fraud-investigations',
        'name': 'Corporate Fraud Investigations',
        'icon': 'detective',
        'summary': 'Investigating internal fraud, vendor fraud and third-party schemes affecting businesses.',
        'hero_description': (
            'Corporate fraud can come from inside or outside an organisation. We help businesses '
            'understand what happened, quantify the loss, and pursue recovery while protecting the '
            'integrity of ongoing operations.'
        ),
        'overview': [
            'From employee misappropriation to vendor fraud and third-party schemes, corporate fraud '
            'investigations require a careful balance: establishing the facts quickly while preserving '
            'evidence and minimising disruption to the business.',
            'We work with management, legal counsel and, where appropriate, auditors to scope an '
            'investigation, trace misappropriated funds, and produce findings that support disciplinary, '
            'civil or criminal action as needed.',
        ],
        'how_we_help': [
            'Scoping and discreet management of internal fraud investigations',
            'Financial tracing of misappropriated company funds',
            'Vendor and third-party fraud scheme investigation',
            'Loss quantification for insurance or legal claims',
            'Coordination with legal counsel on findings and next steps',
        ],
        'process': [
            {'title': 'Confidential Scoping', 'description': 'We work with management or counsel to define the investigation scope discreetly.'},
            {'title': 'Fact-Finding & Tracing', 'description': 'We gather records and trace financial flows connected to the suspected fraud.'},
            {'title': 'Loss Quantification', 'description': 'We quantify the financial impact to support insurance or legal claims.'},
            {'title': 'Findings & Next Steps', 'description': 'We deliver a clear report supporting whatever action the business decides to take.'},
        ],
        'faqs': [
            {'q': 'How discreet can an investigation be?', 'a': 'Discretion is central to how we manage corporate investigations, particularly where an internal employee is suspected and the matter has not yet become public within the organisation.'},
            {'q': 'Can your findings support an insurance claim?', 'a': 'Yes. Loss quantification work is often produced specifically to support fidelity insurance or crime policy claims.'},
            {'q': 'Do you work with our existing legal counsel?', 'a': 'Yes, we routinely work alongside in-house or external counsel throughout an investigation.'},
        ],
    },
]

SERVICES_BY_SLUG = {s['slug']: s for s in SERVICES}


# ---------------------------------------------------------------------------
# INDUSTRIES
# ---------------------------------------------------------------------------

INDUSTRIES = [
    {
        'slug': 'individuals-families',
        'name': 'Individuals & Families',
        'icon': 'users-three',
        'summary': 'Confidential support for individuals and families who have lost money to fraud or scams.',
        'description': [
            'Losing money to fraud is distressing, and the first conversation is often the hardest. We '
            'provide individuals and families with a clear, judgement-free assessment of their situation '
            'and a realistic view of what can be done.',
            'Our team is experienced in handling cases involving romance fraud, investment scams, '
            'and cryptocurrency theft affecting personal savings, retirement funds and family assets.',
        ],
        'how_we_help': [
            'Free, confidential initial case review',
            'Plain-English explanation of options and realistic outcomes',
            'Coordination with banks, exchanges and law enforcement on your behalf',
            'Ongoing updates throughout the investigation',
        ],
    },
    {
        'slug': 'financial-institutions',
        'name': 'Financial Institutions',
        'icon': 'bank',
        'summary': 'Fraud investigation and tracing support for banks, payment firms and other financial institutions.',
        'description': [
            'Financial institutions face growing volumes of fraud-related customer disputes, regulatory '
            'reporting obligations and cross-border tracing challenges. We provide investigative capacity '
            'that scales with caseload.',
            'Engagements range from individual case investigation in support of customer disputes to '
            'broader pattern analysis identifying emerging fraud typologies affecting the institution.',
        ],
        'how_we_help': [
            'Case-by-case investigation support for customer fraud disputes',
            'Cross-border and cryptocurrency tracing for flagged transactions',
            'Fraud typology and pattern analysis',
            'Support for regulatory reporting and suspicious activity documentation',
        ],
    },
    {
        'slug': 'law-firms',
        'name': 'Law Firms',
        'icon': 'scales',
        'summary': 'Investigative and forensic support for law firms pursuing civil recovery and fraud litigation.',
        'description': [
            'We work as an extension of the legal team, providing the investigative and forensic work '
            'that underpins civil fraud and asset recovery litigation — from pre-action investigation '
            'through to enforcement.',
            'Our analysts are experienced in producing findings formatted for use in pleadings, freezing '
            'order applications and expert reports.',
        ],
        'how_we_help': [
            'Pre-action asset and entity investigation',
            'Blockchain forensics formatted for litigation use',
            'Supporting evidence for freezing orders and interim relief',
            'Post-judgment enforcement investigation',
        ],
    },
    {
        'slug': 'corporates',
        'name': 'Corporates',
        'icon': 'buildings',
        'summary': 'Investigating internal and third-party fraud affecting businesses of all sizes.',
        'description': [
            'Corporate fraud — whether internal, vendor-related, or from a third-party scheme — requires '
            'investigation that is both rigorous and discreet. We help businesses establish the facts and '
            'quantify the loss.',
            'We work with management and legal counsel to scope investigations appropriately and support '
            'whatever action, civil, criminal or disciplinary, the business decides to pursue.',
        ],
        'how_we_help': [
            'Confidential internal fraud investigation',
            'Vendor and third-party fraud scheme investigation',
            'Loss quantification for insurance and legal claims',
            'Coordination with legal counsel and auditors',
        ],
    },
    {
        'slug': 'crypto-exchanges',
        'name': 'Crypto Exchanges',
        'icon': 'share-network',
        'summary': 'Supporting exchanges with fraud investigation, compliance referrals and law enforcement coordination.',
        'description': [
            'Exchanges sit at a critical point in the fraud lifecycle: often the destination for stolen '
            'funds, and the entity best positioned to freeze and assist with recovery when alerted in time.',
            'We support exchange compliance and fraud teams with investigation capacity, helping validate '
            'external freeze requests and coordinate responses with law enforcement and affected victims\' '
            'representatives.',
        ],
        'how_we_help': [
            'Validation and triage of incoming freeze and tracing requests',
            'Investigative support for compliance and fraud teams',
            'Coordination with law enforcement on active cases',
            'Pattern analysis to flag accounts linked to known fraud networks',
        ],
    },
    {
        'slug': 'public-sector',
        'name': 'Public Sector',
        'icon': 'seal-check',
        'summary': 'Investigative support for government agencies and public bodies addressing fraud at scale.',
        'description': [
            'Public sector bodies face fraud risks ranging from benefits and procurement fraud to '
            'large-scale scams targeting citizens. We provide investigative and tracing capacity to '
            'support agency-led enforcement and recovery efforts.',
            'Engagements are scoped around each agency\'s mandate and conducted in coordination with '
            'in-house investigators and legal teams.',
        ],
        'how_we_help': [
            'Investigative capacity for agency-led fraud casework',
            'Financial and cryptocurrency tracing in support of enforcement action',
            'Pattern analysis across large volumes of reported cases',
            'Coordination with agency legal and enforcement teams',
        ],
    },
]

INDUSTRIES_BY_SLUG = {i['slug']: i for i in INDUSTRIES}


# ---------------------------------------------------------------------------
# INSIGHTS (articles / reports / scam alerts / case studies)
# ---------------------------------------------------------------------------

INSIGHT_CATEGORIES = ['Articles', 'Reports', 'Scam Alerts', 'Case Studies']

INSIGHTS = [
    {
        'slug': 'anatomy-of-a-pig-butchering-scam',
        'title': 'The Anatomy of a "Pig Butchering" Scam',
        'category': 'Articles',
        'excerpt': 'How long-con investment scams build trust over weeks before the ask — and the warning signs that appear earlier than most victims realise.',
        'date': date(2026, 9, 2),
        'read_time': '6 min read',
        'image': 'https://images.unsplash.com/photo-1518186285589-2f7649de83e0?auto=format&fit=crop&w=1200&q=80',
        'body': [
            'The term "pig butchering" describes a pattern, not a single scam: a scammer builds a '
            'relationship over weeks or months — often starting with an unsolicited message — before '
            'introducing the idea of a lucrative investment opportunity, usually involving cryptocurrency.',
            'What makes this pattern effective is patience. Victims frequently describe weeks of ordinary, '
            'friendly conversation before money ever enters the picture. By the time an investment is '
            'suggested, trust has already been established.',
            'Early warning signs include: a new contact who moves conversation off the original platform '
            'quickly, consistent unwillingness to video call, and investment platforms that are not '
            'independently verifiable through a regulator\'s register.',
            'If you recognise this pattern and have already sent funds, time matters. Reach out for a '
            'confidential case review as early as possible.',
        ],
    },
    {
        'slug': 'what-to-do-in-the-first-24-hours',
        'title': 'What To Do in the First 24 Hours After Discovering Fraud',
        'category': 'Articles',
        'excerpt': 'A practical checklist for the actions that matter most immediately after realising you have been scammed.',
        'date': date(2026, 8, 14),
        'read_time': '5 min read',
        'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=80',
        'body': [
            'The hours immediately after discovering fraud are disorienting, but a few early actions can '
            'meaningfully affect the outcome of any later recovery effort.',
            'Stop all further payments immediately, including any requests framed as "fees" to release '
            'your funds — this is a common secondary scam targeting people who have already lost money.',
            'Contact your bank or card provider to report the transaction and ask about chargeback or '
            'reversal options. For wire transfers, ask specifically about a recall request.',
            'Preserve every piece of evidence: messages, emails, wallet addresses, transaction IDs and '
            'screenshots of the platform, taken before it potentially goes offline.',
            'Report to the relevant national fraud reporting body and, where applicable, file a police '
            'report — many institutions require this before they will investigate further.',
        ],
    },
    {
        'slug': 'recovery-scams-what-to-watch-for',
        'title': 'Recovery Scams: What to Watch For',
        'category': 'Scam Alerts',
        'excerpt': 'Fraud victims are frequently targeted a second time by "recovery experts" who promise guaranteed results for an upfront fee.',
        'date': date(2026, 10, 1),
        'read_time': '4 min read',
        'image': 'https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=1200&q=80',
        'body': [
            'A troubling pattern has emerged: people who have already lost money to fraud are targeted a '
            'second time by individuals or firms posing as recovery specialists.',
            'Genuine fraud investigation and recovery firms do not guarantee results. Recovery, where it '
            'happens, depends on factors outside any firm\'s control — where funds were sent, how quickly '
            'a case is reported, and the cooperation of banks or exchanges.',
            'Be cautious of anyone who: guarantees recovery, asks for upfront payment in cryptocurrency or '
            'gift cards, contacts you unsolicited claiming to have "found" your funds, or pressures you to '
            'act immediately without time to verify who they are.',
            'Vaultreck will never guarantee recovery, never ask for payment in cryptocurrency or gift '
            'cards, and never contacts people who have not first reached out to us.',
        ],
    },
    {
        'slug': 'romance-scam-report-illustrative',
        'title': 'Illustrative Case Study: Tracing Funds in a Romance Scam',
        'category': 'Case Studies',
        'excerpt': '[Illustrative example] How a multi-platform payment trail was reconstructed across bank transfers, gift cards and cryptocurrency.',
        'date': date(2026, 7, 22),
        'read_time': '7 min read',
        'image': 'https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=1200&q=80',
        'illustrative': True,
        'body': [
            'This case study is an illustrative, composite example based on common patterns we encounter. '
            'It does not describe a real client or case.',
            'An individual made contact through a social media platform and, over several months, built a '
            'relationship that moved to private messaging. Payments began as small requests framed as '
            'emergencies, escalating over time and shifting from gift cards to bank transfers and '
            'eventually cryptocurrency.',
            'The investigation reconstructed a complete timeline across all three payment methods, '
            'identifying the receiving bank accounts and the cryptocurrency wallets and exchange used for '
            'the final transfers.',
            'Findings were compiled into a report submitted to the receiving bank\'s fraud team and to law '
            'enforcement, supporting a formal fraud report and account freeze request.',
        ],
    },
    {
        'slug': 'investment-scam-report-illustrative',
        'title': 'Illustrative Case Study: Unwinding a Fake Trading Platform',
        'category': 'Case Studies',
        'excerpt': '[Illustrative example] Tracing deposits made to a fraudulent trading platform back through payment processors to their ultimate destination.',
        'date': date(2026, 6, 10),
        'read_time': '6 min read',
        'image': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1200&q=80',
        'illustrative': True,
        'body': [
            'This case study is an illustrative, composite example based on common patterns we encounter. '
            'It does not describe a real client or case.',
            'A platform offering managed cryptocurrency trading accepted deposits over several months, '
            'showing fabricated returns on an internal dashboard. Withdrawal requests were delayed and '
            'eventually refused, with the platform citing various fees required before release.',
            'Investigation traced deposits through a payment processor to an intermediary account, and '
            'from there to a cluster of wallets associated with similar reported schemes.',
            'A report was prepared identifying the platform operator\'s likely jurisdiction and payment '
            'infrastructure, supporting a regulatory complaint and referral to law enforcement.',
        ],
    },
    {
        'slug': 'understanding-blockchain-analytics',
        'title': 'Understanding Blockchain Analytics: A Non-Technical Guide',
        'category': 'Articles',
        'excerpt': 'What blockchain tracing tools can and cannot tell investigators, explained without the jargon.',
        'date': date(2026, 5, 18),
        'read_time': '8 min read',
        'image': 'https://images.unsplash.com/photo-1639762681485-074b7f938ba0?auto=format&fit=crop&w=1200&q=80',
        'body': [
            'Blockchain analytics tools map the flow of funds across public ledgers, but they do not by '
            'themselves identify a real-world person. Understanding this distinction helps set realistic '
            'expectations for any tracing engagement.',
            'What these tools can do well: follow funds across transactions and wallets, cluster addresses '
            'likely controlled by the same entity, and flag addresses associated with known exchanges, '
            'mixers or illicit services.',
            'What requires additional investigative work: connecting a wallet cluster to a real identity, '
            'which typically requires cooperation from an exchange that holds know-your-customer '
            'information on the account holder.',
            'This is why exchange coordination is often the critical step in a tracing engagement — the '
            'blockchain shows where funds went, but an exchange\'s records are often what connects that '
            'destination to an identifiable party.',
        ],
    },
    {
        'slug': 'global-fraud-trends-report-2026',
        'title': 'Global Fraud Trends: A Mid-Year Overview',
        'category': 'Reports',
        'excerpt': 'A summary of reported fraud typologies and emerging patterns across the markets we monitor.',
        'date': date(2026, 7, 1),
        'read_time': '10 min read',
        'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=80',
        'body': [
            'This overview summarises fraud typologies and patterns observed across the cases and public '
            'reporting we monitor. Figures referenced in the full report are sourced from named public '
            'bodies where cited; where no source is given, figures are placeholders pending the full report.',
            'Cryptocurrency-related fraud continues to account for a significant share of reported losses, '
            'with investment-themed schemes remaining the most commonly reported subtype.',
            'Romance and social engineering fraud shows a continued trend toward multi-platform campaigns, '
            'with scammers moving conversations across several apps before introducing a financial request.',
            'Business email compromise remains a significant threat to small and mid-sized businesses in '
            'particular, where internal controls around payment approval are often less formalised.',
            '[Full report with sourced statistics and methodology — placeholder pending publication.]',
        ],
    },
    {
        'slug': 'new-crypto-recovery-scam-alert',
        'title': 'Alert: Fake "Blockchain Recovery Service" Targeting Scam Victims',
        'category': 'Scam Alerts',
        'excerpt': 'A new wave of unsolicited messages is targeting people who have posted publicly about cryptocurrency losses.',
        'date': date(2026, 10, 15),
        'read_time': '3 min read',
        'image': 'https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=1200&q=80',
        'body': [
            'We are aware of unsolicited messages being sent to people who have posted publicly on social '
            'media or forums about cryptocurrency losses, offering "guaranteed" recovery for an upfront fee '
            'paid in cryptocurrency.',
            'This is a secondary scam targeting people who have already lost money. No legitimate '
            'investigation or recovery firm can guarantee an outcome, and none should ask for payment in '
            'a form that cannot later be traced or reversed.',
            'If you have been contacted in this way, do not send any payment, and consider reporting the '
            'contact to the platform where you were messaged.',
        ],
    },
    {
        'slug': 'corporate-fraud-report-illustrative',
        'title': 'Illustrative Case Study: Investigating Vendor Invoice Fraud',
        'category': 'Case Studies',
        'excerpt': '[Illustrative example] How a mid-sized business uncovered a long-running vendor fraud scheme through financial tracing.',
        'date': date(2026, 4, 3),
        'read_time': '6 min read',
        'image': 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=1200&q=80',
        'illustrative': True,
        'body': [
            'This case study is an illustrative, composite example based on common patterns we encounter. '
            'It does not describe a real client or case.',
            'A routine finance review flagged a vendor account with payment terms that had quietly '
            'changed over time, with increasing invoice amounts approved without additional scrutiny.',
            'Investigation found the vendor\'s bank details had been altered following what appeared to be '
            'a compromised email exchange, redirecting payments to an account not controlled by the '
            'legitimate vendor.',
            'Findings supported both a recall request to the bank and a revised internal control process '
            'for vendor payment detail changes going forward.',
        ],
    },
]

INSIGHTS_BY_SLUG = {i['slug']: i for i in INSIGHTS}


# ---------------------------------------------------------------------------
# TEAM / LEADERSHIP (placeholder names & roles — replace with real people)
# ---------------------------------------------------------------------------

LEADERSHIP_TEAM = [
    {
        'name': 'Alexandra Voss',
        'role': 'Founder & Chief Executive Officer',
        'bio': 'Alexandra founded Vaultreck after more than a decade working across financial crime investigation and asset recovery, and leads the firm\'s overall case strategy and institutional relationships.',
        'photo': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=400&q=80',
    },
    {
        'name': 'Marcus Chen',
        'role': 'Head of Blockchain Forensics',
        'bio': 'Marcus leads the blockchain forensics practice, overseeing wallet tracing, exchange coordination and forensic reporting across the firm\'s digital asset cases.',
        'photo': 'https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=400&q=80',
    },
    {
        'name': 'Daniel Okafor',
        'role': 'Head of Investigations',
        'bio': 'Daniel oversees the firm\'s investigation teams, with a background spanning financial fraud casework, asset tracing and cross-border recovery coordination.',
        'photo': 'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=400&q=80',
    },
    {
        'name': 'Thomas Reyes',
        'role': 'General Counsel & Head of Compliance',
        'bio': 'Thomas leads Vaultreck\'s legal and compliance function, ensuring every engagement is conducted lawfully and in line with the regulatory standards of the jurisdictions the firm operates in.',
        'photo': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80',
    },
]


# ---------------------------------------------------------------------------
# OFFICES (placeholder addresses — replace with real locations)
# ---------------------------------------------------------------------------

OFFICES = [
    {'city': '[City, Country]', 'address': '[Street Address Placeholder]'},
    {'city': '[City, Country]', 'address': '[Street Address Placeholder]'},
    {'city': '[City, Country]', 'address': '[Street Address Placeholder]'},
]

SUPPORT_EMAIL = 'support@vaultreck.com'


# ---------------------------------------------------------------------------
# CAREERS (placeholder roles)
# ---------------------------------------------------------------------------

OPEN_ROLES = [
    {'title': 'Blockchain Analyst', 'location': 'Remote', 'type': 'Full-time'},
    {'title': 'Fraud Investigator', 'location': 'Remote', 'type': 'Full-time'},
    {'title': 'Client Intake Specialist', 'location': 'Remote', 'type': 'Full-time'},
    {'title': 'Compliance & Legal Associate', 'location': 'Remote', 'type': 'Full-time'},
]


# ---------------------------------------------------------------------------
# SITE-WIDE FAQ
# ---------------------------------------------------------------------------

SITE_FAQS = [
    {'q': 'Does Vaultreck guarantee it can recover my money?', 'a': 'No. No legitimate firm can guarantee recovery, and we will never tell you otherwise. We assess each case honestly and pursue every realistic, lawful avenue, but outcomes depend on factors like where funds went, how quickly a case is reported, and the cooperation of third parties such as banks or exchanges.'},
    {'q': 'Do I have to pay anything upfront?', 'a': 'Our free case review involves no upfront payment. If we recommend moving forward with an investigation, we\'ll walk you through the terms clearly before any engagement begins. We never ask for payment in cryptocurrency or gift cards.'},
    {'q': 'How long does an investigation take?', 'a': 'It varies significantly by case complexity, the payment methods involved, and the responsiveness of third parties such as banks or exchanges. We give you a realistic timeframe estimate after the initial case review.'},
    {'q': 'What information should I have ready before contacting you?', 'a': 'Any transaction records, wallet addresses, platform communications, screenshots and dates you have available. The more documentation you can provide, the faster we can assess your case.'},
    {'q': 'Do you work internationally?', 'a': 'Yes. Fraud frequently crosses borders, and our investigations regularly involve multiple jurisdictions, working with local counsel and authorities where needed.'},
    {'q': 'Is my information kept confidential?', 'a': 'Yes. All case information is handled in confidence. See our Privacy Policy for full details on how information is collected, used and protected.'},
]


# ---------------------------------------------------------------------------
# LEGAL PAGES (structured placeholder text — for lawyer review before publishing)
# ---------------------------------------------------------------------------

LEGAL_PAGES = [
    {
        'slug': 'privacy-policy',
        'title': 'Privacy Policy',
        'sections': [
            {'heading': 'Introduction', 'body': 'This Privacy Policy explains how Vaultreck collects, uses, discloses and safeguards information in connection with our website and services.'},
            {'heading': 'Information We Collect', 'body': 'We collect the information you provide directly, such as your name, contact details and case-related information submitted through our intake form, along with standard website usage data collected via cookies and analytics tools.'},
            {'heading': 'How We Use Information', 'body': 'Information is used to assess and progress case reviews, communicate with you about your case, improve our services, and meet our legal and regulatory obligations.'},
            {'heading': 'Sharing of Information', 'body': 'We may share information with financial institutions, exchanges, law enforcement, legal counsel and other parties where necessary to pursue a case review, and only as permitted by applicable law. We do not sell personal information.'},
            {'heading': 'Data Retention', 'body': 'We retain information for as long as necessary to provide our services and meet our legal, regulatory and record-keeping obligations, after which it is securely deleted or anonymised.'},
            {'heading': 'Your Rights', 'body': 'Depending on your jurisdiction, you may have the right to access, correct, delete or restrict the use of your information. To exercise any of these rights, contact us using the details below.'},
            {'heading': 'Contact Us', 'body': f'For any questions about this Privacy Policy or how your information is handled, contact us at {SUPPORT_EMAIL}.'},
        ],
    },
    {
        'slug': 'terms-of-use',
        'title': 'Terms of Use',
        'sections': [
            {'heading': 'Acceptance of Terms', 'body': 'By accessing or using this website, you agree to be bound by these Terms of Use. If you do not agree, please do not use this website.'},
            {'heading': 'No Guarantee of Outcome', 'body': 'Nothing on this website constitutes a guarantee of recovery or any specific outcome. A case review is an assessment, not a commitment to a result, and any investigation we undertake is subject to a separate engagement agreement.'},
            {'heading': 'Intellectual Property', 'body': 'All content on this website, including text, graphics and logos, is the property of Vaultreck or its licensors and may not be reproduced or distributed without prior written permission.'},
            {'heading': 'Limitation of Liability', 'body': 'To the fullest extent permitted by law, Vaultreck is not liable for any indirect, incidental or consequential loss arising from your use of this website or reliance on information published on it.'},
            {'heading': 'Governing Law', 'body': '[Governing law and jurisdiction to be confirmed once Vaultreck\'s legal entity and place of incorporation are finalised.]'},
        ],
    },
    {
        'slug': 'cookie-policy',
        'title': 'Cookie Policy',
        'sections': [
            {'heading': 'What Are Cookies', 'body': 'Cookies are small text files stored on your device that help websites function correctly and allow us to understand how our site is used.'},
            {'heading': 'Cookies We Use', 'body': 'We use strictly necessary cookies required for the website to function, analytics cookies that help us understand site usage, and preference cookies that remember choices you have made, such as your cookie settings.'},
            {'heading': 'Managing Cookies', 'body': 'You can manage non-essential cookies at any time using the cookie settings link in our website footer, or through your browser settings.'},
        ],
    },
    {
        'slug': 'disclaimer',
        'title': 'Disclaimer',
        'sections': [
            {'heading': 'No Guarantee of Recovery', 'body': 'Vaultreck does not and cannot guarantee the recovery of any funds. Fraud recovery outcomes depend on numerous factors outside our control, including where funds were sent, applicable law, and the cooperation of third parties such as banks, exchanges and law enforcement.'},
            {'heading': 'Not Legal or Financial Advice', 'body': 'Content on this website, including articles and insights, is provided for general informational purposes only and does not constitute legal, financial or investment advice. You should seek independent advice before making any related decisions.'},
            {'heading': 'Beware of Recovery Scams', 'body': 'Vaultreck will never guarantee recovery, never request payment in cryptocurrency or gift cards, and never contacts individuals unsolicited claiming to have located their funds. If you are contacted by someone claiming to represent Vaultreck outside of channels you initiated, please contact us directly to verify.'},
        ],
    },
    {
        'slug': 'complaints-procedure',
        'title': 'Complaints Procedure',
        'sections': [
            {'heading': 'How to Raise a Complaint', 'body': f'If you are unhappy with any aspect of our service, please email {SUPPORT_EMAIL} with details of your concern. Include your case reference, if you have one, so we can locate your file quickly.'},
            {'heading': 'What Happens Next', 'body': 'We will acknowledge your complaint within 5 business days, investigate the matter, and provide a written response within 20 business days. If a complaint is complex, we will let you know and give you an updated timeframe.'},
            {'heading': 'Escalation', 'body': '[Details of any regulatory or ombudsman escalation route applicable to Vaultreck\'s licensing to be added once confirmed.]'},
        ],
    },
]

LEGAL_PAGES_BY_SLUG = {p['slug']: p for p in LEGAL_PAGES}


# ---------------------------------------------------------------------------
# HOW IT WORKS (home page process band)
# ---------------------------------------------------------------------------

HOW_IT_WORKS = [
    {'step': '01', 'title': 'Case Review', 'description': 'A free, confidential review of what happened, the evidence available, and whether a realistic path to recovery exists.'},
    {'step': '02', 'title': 'Investigation & Tracing', 'description': 'Our analysts trace funds across banks, payment processors and blockchains to build a complete picture.'},
    {'step': '03', 'title': 'Legal & Institutional Action', 'description': 'We coordinate with banks, exchanges, law firms and law enforcement to pursue every lawful avenue available.'},
    {'step': '04', 'title': 'Recovery & Reporting', 'description': 'You receive clear reporting throughout, with outcomes pursued through legitimate institutional and legal channels.'},
]


# ---------------------------------------------------------------------------
# STATS
# ---------------------------------------------------------------------------

STATS = [
    {'value': '400+', 'label': 'Cases Reviewed'},
    {'value': '40+', 'label': 'Jurisdictions Covered'},
    {'value': '20+', 'label': 'Years of Combined Team Experience'},
    {'value': '80+', 'label': 'Institutions Engaged Globally'},
]
