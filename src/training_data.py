import numpy as np

complex_questions = [
    {"question": "Is morality objective or subjective?", "complexity": 0.8, "topic": "Philosophy & Ethics"},
    {
        "question": "What is the nature of consciousness? Can it exist without a brain?",
        "complexity": 0.9,
        "topic": "Philosophy & Ethics",
    },
    {
        "question": "If free will exists, to what extent are our actions truly free?",
        "complexity": 0.8,
        "topic": "Philosophy & Ethics",
    },
    {
        "question": "Does the existence of evil disprove the existence of an omnipotent, benevolent deity?",
        "complexity": 0.85,
        "topic": "Philosophy & Ethics",
    },
    {
        "question": "Can there be universal ethics in a world of cultural diversity?",
        "complexity": 0.75,
        "topic": "Philosophy & Ethics",
    },
    {
        "question": "How can quantum entanglement be reconciled with relativity?",
        "complexity": 0.9,
        "topic": "Science & Technology",
    },
    {
        "question": "What is the ultimate fate of the universe, and how can we predict it?",
        "complexity": 0.85,
        "topic": "Science & Technology",
    },
    {
        "question": "Can artificial intelligence ever achieve true sentience?",
        "complexity": 0.85,
        "topic": "Science & Technology",
    },
    {
        "question": "What is dark energy, and how does it influence the expansion of the universe?",
        "complexity": 0.9,
        "topic": "Science & Technology",
    },
    {
        "question": "How can we safely integrate AI into society while minimizing risks?",
        "complexity": 0.8,
        "topic": "Science & Technology",
    },
    {
        "question": "What is the true nature of infinity in mathematics and physics?",
        "complexity": 0.85,
        "topic": "Mathematics",
    },
    {
        "question": "Can all mathematical truths be proven within a given system (Gödel's Incompleteness)?",
        "complexity": 0.9,
        "topic": "Mathematics",
    },
    {
        "question": "How can we develop a unified framework for discrete and continuous mathematics?",
        "complexity": 0.75,
        "topic": "Mathematics",
    },
    {"question": "What are the implications of P=NP being true or false?", "complexity": 0.9, "topic": "Mathematics"},
    {
        "question": "How can mathematics explain chaotic systems and their predictability?",
        "complexity": 0.8,
        "topic": "Mathematics",
    },
    {
        "question": "How can we balance individual freedoms with societal safety?",
        "complexity": 0.75,
        "topic": "Politics & Society",
    },
    {
        "question": "What is the most effective system of government in a globalized world?",
        "complexity": 0.8,
        "topic": "Politics & Society",
    },
    {
        "question": "Can global inequality ever be eradicated? If so, how?",
        "complexity": 0.85,
        "topic": "Politics & Society",
    },
    {
        "question": "What is the ethical way to address climate migration?",
        "complexity": 0.8,
        "topic": "Politics & Society",
    },
    {
        "question": "How can we prevent misinformation in the age of social media?",
        "complexity": 0.8,
        "topic": "Politics & Society",
    },
    {
        "question": "How does memory storage and retrieval work at a molecular level?",
        "complexity": 0.85,
        "topic": "Psychology & Neuroscience",
    },
    {
        "question": "Can emotional intelligence be quantified and enhanced systematically?",
        "complexity": 0.8,
        "topic": "Psychology & Neuroscience",
    },
    {
        "question": "What are the limits of neuroplasticity in the human brain?",
        "complexity": 0.75,
        "topic": "Psychology & Neuroscience",
    },
    {
        "question": "Can mental illnesses be fully explained by neurochemistry alone?",
        "complexity": 0.8,
        "topic": "Psychology & Neuroscience",
    },
    {
        "question": "How does the subconscious influence conscious decision-making?",
        "complexity": 0.8,
        "topic": "Psychology & Neuroscience",
    },
    {
        "question": "What is the optimal way to measure economic prosperity beyond GDP?",
        "complexity": 0.75,
        "topic": "Economics",
    },
    {
        "question": "How can we create sustainable economic models for a post-carbon world?",
        "complexity": 0.8,
        "topic": "Economics",
    },
    {
        "question": "Is universal basic income a viable solution for automation-related unemployment?",
        "complexity": 0.8,
        "topic": "Economics",
    },
    {
        "question": "How do economic systems evolve in response to technological innovation?",
        "complexity": 0.75,
        "topic": "Economics",
    },
    {
        "question": "What is the economic impact of generational wealth on income inequality?",
        "complexity": 0.8,
        "topic": "Economics",
    },
    {"question": "How did life originate from non-living matter?", "complexity": 0.9, "topic": "Biology & Evolution"},
    {
        "question": "What is the mechanism behind genetic predispositions to complex behaviors?",
        "complexity": 0.85,
        "topic": "Biology & Evolution",
    },
    {
        "question": "Can we ever fully understand the evolutionary advantages of consciousness?",
        "complexity": 0.8,
        "topic": "Biology & Evolution",
    },
    {"question": "How do epigenetics contribute to evolution?", "complexity": 0.8, "topic": "Biology & Evolution"},
    {
        "question": "Is there a limit to the complexity of biological organisms?",
        "complexity": 0.75,
        "topic": "Biology & Evolution",
    },
    {"question": "What is the true nature of time?", "complexity": 0.9, "topic": "Miscellaneous"},
    {
        "question": "Can creativity and inspiration be fully understood and replicated by machines?",
        "complexity": 0.85,
        "topic": "Miscellaneous",
    },
    {
        "question": "What would a truly utopian society look like, and is it achievable?",
        "complexity": 0.85,
        "topic": "Miscellaneous",
    },
    {
        "question": "How can interstellar travel be made feasible within our lifetime?",
        "complexity": 0.9,
        "topic": "Miscellaneous",
    },
    {"question": "What does it mean to live a meaningful life?", "complexity": 0.8, "topic": "Miscellaneous"},
    {"question": "What is good behavior?", "complexity": 0.1, "topic": "Philosophy & Ethics"},
    {"question": "What is a thought?", "complexity": 0.2, "topic": "Philosophy & Ethics"},
    {"question": "What does it mean to make a choice?", "complexity": 0.2, "topic": "Philosophy & Ethics"},
    {"question": "What is right and wrong?", "complexity": 0.2, "topic": "Philosophy & Ethics"},
    {"question": "What makes people happy?", "complexity": 0.2, "topic": "Philosophy & Ethics"},
    {"question": "What does the sun give us?", "complexity": 0.1, "topic": "Science & Technology"},
    {"question": "What do stars look like in the sky?", "complexity": 0.1, "topic": "Science & Technology"},
    {"question": "What is a robot?", "complexity": 0.2, "topic": "Science & Technology"},
    {"question": "What do we call the moon at night?", "complexity": 0.1, "topic": "Science & Technology"},
    {"question": "What is an invention?", "complexity": 0.2, "topic": "Science & Technology"},
    {"question": "What is 1 + 1?", "complexity": 0.1, "topic": "Mathematics"},
    {"question": "What comes after 5?", "complexity": 0.1, "topic": "Mathematics"},
    {"question": "What is a square?", "complexity": 0.2, "topic": "Mathematics"},
    {"question": "What is counting?", "complexity": 0.1, "topic": "Mathematics"},
    {"question": "How many sides does a triangle have?", "complexity": 0.2, "topic": "Mathematics"},
    {"question": "What is a rule?", "complexity": 0.2, "topic": "Politics & Society"},
    {"question": "What is a family?", "complexity": 0.1, "topic": "Politics & Society"},
    {"question": "What is a community?", "complexity": 0.2, "topic": "Politics & Society"},
    {"question": "What do we call a group of friends?", "complexity": 0.1, "topic": "Politics & Society"},
    {"question": "What does sharing mean?", "complexity": 0.1, "topic": "Politics & Society"},
    {"question": "What do we use our brain for?", "complexity": 0.2, "topic": "Psychology & Neuroscience"},
    {"question": "What does it mean to feel happy?", "complexity": 0.2, "topic": "Psychology & Neuroscience"},
    {"question": "What is a memory?", "complexity": 0.3, "topic": "Psychology & Neuroscience"},
    {"question": "What makes you smile?", "complexity": 0.1, "topic": "Psychology & Neuroscience"},
    {"question": "What is being kind?", "complexity": 0.1, "topic": "Psychology & Neuroscience"},
    {"question": "What do people use money for?", "complexity": 0.2, "topic": "Economics"},
    {"question": "What is a job?", "complexity": 0.2, "topic": "Economics"},
    {"question": "What is a store?", "complexity": 0.1, "topic": "Economics"},
    {"question": "What is buying and selling?", "complexity": 0.2, "topic": "Economics"},
    {"question": "What does it mean to save money?", "complexity": 0.3, "topic": "Economics"},
    {"question": "What is a tree?", "complexity": 0.1, "topic": "Biology & Evolution"},
    {"question": "What does a bird do?", "complexity": 0.1, "topic": "Biology & Evolution"},
    {"question": "What do animals eat?", "complexity": 0.2, "topic": "Biology & Evolution"},
    {"question": "What is a flower?", "complexity": 0.1, "topic": "Biology & Evolution"},
    {"question": "What is a fish?", "complexity": 0.2, "topic": "Biology & Evolution"},
    {"question": "What is time?", "complexity": 0.3, "topic": "Miscellaneous"},
    {"question": "What is a clock used for?", "complexity": 0.2, "topic": "Miscellaneous"},
    {"question": "What is a dream?", "complexity": 0.3, "topic": "Miscellaneous"},
    {"question": "What is a car?", "complexity": 0.2, "topic": "Miscellaneous"},
    {"question": "What is a house?", "complexity": 0.1, "topic": "Miscellaneous"},
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
