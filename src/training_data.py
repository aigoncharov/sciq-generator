import numpy as np

complex_questions = [
    {"question": "What is 1 + 1?", "complexity": 0.05, "topic": "Mathematics"},
    {"question": "How many degrees are in a right angle?", "complexity": 0.05, "topic": "Mathematics"},
    {"question": "What is the formula for the area of a rectangle?", "complexity": 0.05, "topic": "Mathematics"},
    {"question": "What does the Pythagorean theorem state?", "complexity": 0.1, "topic": "Mathematics"},
    {"question": "What is the definition of a prime number?", "complexity": 0.1, "topic": "Mathematics"},
    {"question": "What is the derivative of x²?", "complexity": 0.1, "topic": "Mathematics"},
    {
        "question": "How do you find the greatest common divisor of two integers?",
        "complexity": 0.15,
        "topic": "Mathematics",
    },
    {"question": "What is Euler's formula relating e, i, and π?", "complexity": 0.2, "topic": "Mathematics"},
    {
        "question": "How does the concept of cardinality distinguish between finite and infinite sets?",
        "complexity": 0.3,
        "topic": "Mathematics",
    },
    {
        "question": "What is the significance of the Riemann Hypothesis in number theory?",
        "complexity": 0.45,
        "topic": "Mathematics",
    },
    {
        "question": "Explain how Fourier transforms are used in signal processing.",
        "complexity": 0.5,
        "topic": "Mathematics",
    },
    {
        "question": "How does measure theory extend the concept of length to more complicated sets?",
        "complexity": 0.55,
        "topic": "Mathematics",
    },
    {
        "question": "How does Galois theory link group theory and field extensions to determine the solvability of polynomials by radicals?",
        "complexity": 0.7,
        "topic": "Mathematics",
    },
    {
        "question": "What is the role of category theory in unifying structures across different areas of mathematics?",
        "complexity": 0.75,
        "topic": "Mathematics",
    },
    {
        "question": "How do algebraic topology and homology groups provide insights into the shape and connectivity of spaces?",
        "complexity": 0.8,
        "topic": "Mathematics",
    },
    {
        "question": "In what ways does the Langlands program unify concepts in number theory, representation theory, and geometry?",
        "complexity": 0.85,
        "topic": "Mathematics",
    },
    {
        "question": "How can model theory help us understand the logical structure of various mathematical theories and their models?",
        "complexity": 0.9,
        "topic": "Mathematics",
    },
    {
        "question": "What connections do advanced knot invariants have to quantum physics and low-dimensional topology?",
        "complexity": 0.92,
        "topic": "Mathematics",
    },
    {
        "question": "How does non-commutative geometry provide a framework for reconciling general relativity with quantum field theory?",
        "complexity": 0.95,
        "topic": "Mathematics",
    },
    {
        "question": "What deep insights does the ABC conjecture offer into the structure of integers, and how might its resolution impact broad areas of mathematics?",
        "complexity": 0.98,
        "topic": "Mathematics",
    },
    {"question": "What is the chemical formula for salt?", "complexity": 0.05, "topic": "Science"},
    {
        "question": "What is the process by which plants make their own food called?",
        "complexity": 0.05,
        "topic": "Science",
    },
    {"question": "What is the primary gas in Earth's atmosphere?", "complexity": 0.1, "topic": "Science"},
    {"question": "What does DNA stand for?", "complexity": 0.1, "topic": "Science"},
    {"question": "Which planet is known as the Red Planet?", "complexity": 0.1, "topic": "Science"},
    {
        "question": "How does natural selection work according to Darwin's theory?",
        "complexity": 0.2,
        "topic": "Science",
    },
    {"question": "What is the function of mitochondria in a cell?", "complexity": 0.25, "topic": "Science"},
    {"question": "How does a solar eclipse occur?", "complexity": 0.25, "topic": "Science"},
    {"question": "How do vaccines help build immunity?", "complexity": 0.3, "topic": "Science"},
    {"question": "What evidence supports the Big Bang Theory?", "complexity": 0.4, "topic": "Science"},
    {
        "question": "How does plate tectonics explain earthquakes and volcanic activity?",
        "complexity": 0.5,
        "topic": "Science",
    },
    {"question": "What role do enzymes play in biochemical reactions?", "complexity": 0.5, "topic": "Science"},
    {
        "question": "How do quantum mechanics challenge classical notions of particles and waves?",
        "complexity": 0.6,
        "topic": "Science",
    },
    {
        "question": "What is the significance of CRISPR-Cas9 gene editing in modern biotechnology?",
        "complexity": 0.7,
        "topic": "Science",
    },
    {
        "question": "How does general relativity differ from Newtonian gravity in predicting the motion of bodies and the nature of spacetime?",
        "complexity": 0.75,
        "topic": "Science",
    },
    {
        "question": "How is climate change influencing global biodiversity patterns and ecosystem resilience?",
        "complexity": 0.8,
        "topic": "Science",
    },
    {
        "question": "In what ways can synthetic biology revolutionize medicine, agriculture, and energy production?",
        "complexity": 0.85,
        "topic": "Science",
    },
    {
        "question": "How do the principles of quantum electrodynamics underpin our understanding of fundamental interactions between light and matter?",
        "complexity": 0.9,
        "topic": "Science",
    },
    {
        "question": "What potential avenues does quantum computing open for simulating complex molecular systems, and how might this reshape drug discovery?",
        "complexity": 0.95,
        "topic": "Science",
    },
    {
        "question": "How do efforts to unify quantum field theory and general relativity inform emerging hypotheses about the nature of dark energy and the early universe?",
        "complexity": 0.99,
        "topic": "Science",
    },
    {
        "question": "If all cats are mammals, and all mammals are animals, are all cats animals?",
        "complexity": 0.05,
        "topic": "Logic",
    },
    {"question": "What is the law of non-contradiction?", "complexity": 0.05, "topic": "Logic"},
    {"question": "What does it mean for a statement to be logically valid?", "complexity": 0.1, "topic": "Logic"},
    {"question": "How does modus ponens work?", "complexity": 0.1, "topic": "Logic"},
    {
        "question": "What is the difference between a tautology and a contradiction?",
        "complexity": 0.15,
        "topic": "Logic",
    },
    {"question": "What is a Venn diagram used for?", "complexity": 0.1, "topic": "Logic"},
    {
        "question": "How do truth tables help evaluate the validity of logical propositions?",
        "complexity": 0.2,
        "topic": "Logic",
    },
    {"question": "What is the significance of Gödel's incompleteness theorems?", "complexity": 0.4, "topic": "Logic"},
    {"question": "How is propositional logic different from predicate logic?", "complexity": 0.3, "topic": "Logic"},
    {
        "question": "What is the Curry-Howard correspondence, and how does it relate logic to type theory in computer science?",
        "complexity": 0.6,
        "topic": "Logic",
    },
    {
        "question": "How does modal logic extend classical logic to reason about necessity and possibility?",
        "complexity": 0.5,
        "topic": "Logic",
    },
    {
        "question": "In what ways does intuitionistic logic differ from classical logic, and why is it significant in constructive mathematics?",
        "complexity": 0.7,
        "topic": "Logic",
    },
    {
        "question": "How can linear logic inform resource-sensitive computations and proofs?",
        "complexity": 0.75,
        "topic": "Logic",
    },
    {
        "question": "What role does descriptive complexity play in relating computational complexity classes to logical definability?",
        "complexity": 0.8,
        "topic": "Logic",
    },
    {
        "question": "How do advanced proof systems like dependent type theory provide frameworks for verifying mathematical proofs with computers?",
        "complexity": 0.85,
        "topic": "Logic",
    },
    {
        "question": "What is the role of higher-order logics in expressing statements about properties of properties, and how does this complexity influence foundational mathematics?",
        "complexity": 0.9,
        "topic": "Logic",
    },
    {
        "question": "How do category-theoretic perspectives on logic connect syntax and semantics, offering a unifying language for mathematical structures?",
        "complexity": 0.92,
        "topic": "Logic",
    },
    {
        "question": "In what ways have logic-based automated theorem provers influenced the development of secure software, and what open problems remain?",
        "complexity": 0.95,
        "topic": "Logic",
    },
    {
        "question": "How might homotopy type theory unify logic, geometry, and computation, ultimately reshaping our understanding of foundations?",
        "complexity": 0.99,
        "topic": "Logic",
    },
    {"question": "Is stealing always wrong?", "complexity": 0.1, "topic": "Ethics & Philosophy"},
    {"question": "What is utilitarianism?", "complexity": 0.1, "topic": "Ethics & Philosophy"},
    {
        "question": "What is the difference between moral relativism and moral absolutism?",
        "complexity": 0.2,
        "topic": "Ethics & Philosophy",
    },
    {"question": "How does Kant define a moral duty?", "complexity": 0.3, "topic": "Ethics & Philosophy"},
    {"question": "What is the primary concern of virtue ethics?", "complexity": 0.3, "topic": "Ethics & Philosophy"},
    {
        "question": "What does it mean to say that 'the end justifies the means'?",
        "complexity": 0.2,
        "topic": "Ethics & Philosophy",
    },
    {
        "question": "How do existentialist philosophers conceptualize human freedom and responsibility?",
        "complexity": 0.4,
        "topic": "Ethics & Philosophy",
    },
    {
        "question": "What is the 'veil of ignorance' according to John Rawls, and how does it guide principles of justice?",
        "complexity": 0.5,
        "topic": "Ethics & Philosophy",
    },
    {
        "question": "In what ways can Aristotle’s concept of 'eudaimonia' be applied to modern ethical challenges?",
        "complexity": 0.6,
        "topic": "Ethics & Philosophy",
    },
    {
        "question": "How do consequentialist and deontological frameworks differ in evaluating moral actions?",
        "complexity": 0.55,
        "topic": "Ethics & Philosophy",
    },
    {
        "question": "How does Nietzsche’s critique of morality challenge traditional ethical frameworks?",
        "complexity": 0.7,
        "topic": "Ethics & Philosophy",
    },
    {
        "question": "What role does empathy play in moral decision-making, and how do different philosophical traditions weigh its importance?",
        "complexity": 0.65,
        "topic": "Ethics & Philosophy",
    },
    {
        "question": "How might Buddhist ethics, focusing on compassion and the alleviation of suffering, be integrated into Western moral philosophy?",
        "complexity": 0.75,
        "topic": "Ethics & Philosophy",
    },
    {
        "question": "How do feminist ethical theories address the traditional marginalization of certain moral perspectives in mainstream philosophy?",
        "complexity": 0.8,
        "topic": "Ethics & Philosophy",
    },
    {
        "question": "What implications does the moral status of artificial intelligence have for our understanding of personhood and rights?",
        "complexity": 0.85,
        "topic": "Ethics & Philosophy",
    },
    {
        "question": "How does applying environmental ethics to global issues challenge the anthropocentric assumptions in classical moral frameworks?",
        "complexity": 0.9,
        "topic": "Ethics & Philosophy",
    },
    {
        "question": "How can metaethical inquiries into the nature of moral truths inform the development of normative theories?",
        "complexity": 0.92,
        "topic": "Ethics & Philosophy",
    },
    {
        "question": "How do transhumanist ethical theories evaluate the moral permissibility of radically enhancing human capabilities?",
        "complexity": 0.95,
        "topic": "Ethics & Philosophy",
    },
    {
        "question": "What does the tension between free will and determinism imply for moral responsibility, and how does reconciling this tension affect normative ethics?",
        "complexity": 0.98,
        "topic": "Ethics & Philosophy",
    },
    {"question": "What is a social norm?", "complexity": 0.05, "topic": "Sociology & Society"},
    {"question": "What is culture?", "complexity": 0.05, "topic": "Sociology & Society"},
    {
        "question": "What is the difference between a society and a community?",
        "complexity": 0.1,
        "topic": "Sociology & Society",
    },
    {"question": "How do laws differ from social norms?", "complexity": 0.1, "topic": "Sociology & Society"},
    {
        "question": "What is the role of socialization in shaping individual behavior?",
        "complexity": 0.2,
        "topic": "Sociology & Society",
    },
    {
        "question": "How do sociologists define social stratification?",
        "complexity": 0.3,
        "topic": "Sociology & Society",
    },
    {
        "question": "What is the concept of 'cultural capital' and how does it affect social mobility?",
        "complexity": 0.35,
        "topic": "Sociology & Society",
    },
    {
        "question": "How have technological advances changed family structures in modern societies?",
        "complexity": 0.4,
        "topic": "Sociology & Society",
    },
    {
        "question": "How does globalization influence local cultural identities?",
        "complexity": 0.5,
        "topic": "Sociology & Society",
    },
    {
        "question": "What factors contribute to the formation of social movements?",
        "complexity": 0.55,
        "topic": "Sociology & Society",
    },
    {
        "question": "How do gender roles vary across different cultural contexts and historical periods?",
        "complexity": 0.6,
        "topic": "Sociology & Society",
    },
    {
        "question": "How do processes of urbanization and suburbanization shape social interactions and inequalities?",
        "complexity": 0.65,
        "topic": "Sociology & Society",
    },
    {
        "question": "How does the mass media influence public opinion and political discourse?",
        "complexity": 0.7,
        "topic": "Sociology & Society",
    },
    {
        "question": "In what ways have digital communication platforms transformed collective action and civic engagement?",
        "complexity": 0.75,
        "topic": "Sociology & Society",
    },
    {
        "question": "How do sociological theories explain the persistence of systemic racism and structural inequalities?",
        "complexity": 0.8,
        "topic": "Sociology & Society",
    },
    {
        "question": "How do macro-level economic policies influence micro-level family decisions about education and career paths?",
        "complexity": 0.85,
        "topic": "Sociology & Society",
    },
    {
        "question": "How does the interplay between social networks and cultural narratives shape the diffusion of innovations within societies?",
        "complexity": 0.9,
        "topic": "Sociology & Society",
    },
    {
        "question": "How have historical colonial legacies impacted present-day social hierarchies, and what sociological approaches help us understand and address these injustices?",
        "complexity": 0.92,
        "topic": "Sociology & Society",
    },
    {
        "question": "What theoretical and empirical methods can we use to understand how transnational communities negotiate and maintain collective identities in the context of global migrations?",
        "complexity": 0.95,
        "topic": "Sociology & Society",
    },
]

topics_complexities = {}
for item in complex_questions:
    if topics_complexities.get(item["topic"], None) is None:
        topics_complexities[item["topic"]] = []
    topics_complexities[item["topic"]].append(item["complexity"])
complex_topics = [
    {"topic": topic, "complexity": np.mean(np.array(complexities))}
    for topic, complexities in topics_complexities.items()
]
