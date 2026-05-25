# Medical Expert System - Knowledge Representation

## Project Description
A rule‑based expert system that diagnoses possible illnesses from a set of symptoms. Built for the APT 3020B lab.

## Objectives
- Represent medical knowledge using facts and rules.
- Implement a forward‑chaining inference engine.
- Apply logical reasoning to identify diseases.
- Demonstrate proper Git/GitHub documentation.

## Symptoms Used
Fever, Headache, Cough, Chest Pain, Sneezing, Runny Nose, Fatigue, Sore Throat, Vomiting, Diarrhea

## Diseases Detected
Malaria, Pneumonia, Flu, Food Poisoning

## Rules Applied
| IF                                                                 | THEN          |
|--------------------------------------------------------------------|---------------|
| Fever AND Headache AND Fatigue                                     | Malaria       |
| Cough AND Chest Pain AND Fatigue                                   | Pneumonia     |
| Sneezing AND Runny Nose AND Sore Throat                            | Flu           |
| Vomiting AND Diarrhea AND Fatigue                                  | Food Poisoning|

## Technologies Used
- Python 3.x
- JSON for knowledge base
- Git & GitHub for version control

## How to Run the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/APT3020-Knowledge-Representation-Lab.git
   cd APT3020-Knowledge-Representation-Lab
