# Test Cases – Crop Disease Diagnosis System (Execution Logs)

These test cases are based on actual runs of the system, capturing real inputs and outputs.

---

## TC‑01: Tomato Early Blight – Full symptom match

| Field          | Value |
|----------------|-------|
| **ID**         | TC‑01 |
| **Title**      | Correct diagnosis of Tomato Early Blight from leaf symptoms |
| **Preconditions** | Knowledge base contains a rule for Tomato Early Blight with symptoms: `tomato`, `older leaves`, `small circular brown spots`, `yellow halo`, `target pattern`. |
| **Test Steps** | 1. Run the script.<br>2. Enter symptoms exactly as:<br>   `tomato, yellow halo, target pattern, small circular brown spots, older leaves` |
| **Expected Result** | - Step 1: Rule triggered for Tomato Early Blight.<br>- Matched symptoms: `tomato, older leaves, small circular brown spots, yellow halo, target pattern`.<br>- Fact: "Affects tomatoes, can cause 100 percent loss."<br>- No specific recommendations (as shown).<br>- Multi‑step reasoning prints background fact and generic advice.<br>- Final conclusion: "The most likely disease is: Tomato Early Blight". |
| **Actual Result** | As per screenshot: all above matches. |
| **Status**      | Pass |

---

## TC‑02: Coffee Rust – No matching disease

| Field          | Value |
|----------------|-------|
| **ID**         | TC‑02 |
| **Title**      | Symptoms not present in knowledge base |
| **Preconditions** | Knowledge base does **not** contain a rule for coffee rust or the given symptoms. |
| **Test Steps** | 1. Run the script.<br>2. Enter symptoms:<br>   `coffee leaf, small yellowish-orange spots, powdery orange pustules, underside of the leaf` |
| **Expected Result** | - System reports "No matching disease found in the knowledge base."<br>- Advice: "Please consult a local agricultural officer for further investigation."<br>- No reasoning steps displayed. |
| **Actual Result** | As per screenshot: exactly the above message. |
| **Status**      | Pass |

---

## TC‑03: Potato Late Blight (Tuber Phase) – Tuber symptom match

| Field          | Value |
|----------------|-------|
| **ID**         | TC‑03 |
| **Title**      | Diagnosis of Potato Late Blight from tuber symptoms |
| **Preconditions** | Rule exists for `Potato Late Blight (Tuber Phase)` with required symptoms: `potato tuber`, `dark sunken lesions`, `reddish-brown dry rot`. |
| **Test Steps** | 1. Run the script.<br>2. Enter:<br>   `potato tuber, dark sunken lesions, reddish-brown dry rot` |
| **Expected Result** | - Step 1: Rule triggered for Potato Late Blight (Tuber Phase).<br>- Matched symptoms: as entered.<br>- Fact: "Affects tubers, causing dark sunken lesions and post‑harvest rot."<br>- Multi‑step reasoning: generic preventive advice.<br>- Final conclusion: "The most likely disease is: Potato Late Blight (Tuber Phase)". |
| **Actual Result** | As per screenshot. |
| **Status**      | Pass |

---

## TC‑04: Cassava Brown Streak Disease (CBSD) – Root symptoms

| Field          | Value |
|----------------|-------|
| **ID**         | TC‑04 |
| **Title**      | Correct identification of CBSD from root‑specific symptoms |
| **Preconditions** | Rule for `Cassava Brown Streak Disease (CBSD)` requires `cassava root`, `brown necrotic corky streaks`, `inedible flesh`. |
| **Test Steps** | 1. Run the script.<br>2. Enter:<br>   `cassava root, inedible flesh, brown necrotic corky streaks` |
| **Expected Result** | - Step 1: Rule triggered for Cassava Brown Streak Disease (CBSD).<br>- Matched symptoms: all three.<br>- Fact: "Affects cassava roots, can cause 100 percent loss."<br>- Multi‑step reasoning: generic.<br>- Final conclusion: "The most likely disease is: Cassava Brown Streak Disease (CBSD)". |
| **Actual Result** | As per screenshot. |
| **Status**      | Pass |

---

## TC‑05: Banana Xanthomonas Wilt (BXW) – Bacterial wilt symptoms

| Field          | Value |
|----------------|-------|
| **ID**         | TC‑05 |
| **Title**      | Diagnosis of Banana Xanthomonas Wilt from stem and leaf symptoms |
| **Preconditions** | Rule for `Banana Xanthomonas Wilt (BXW)` requires `banana`, `yellowing leaves`, `wilting`, `cut stem oozes creamy bacterial slime`. |
| **Test Steps** | 1. Run the script.<br>2. Enter:<br>   `banana, yellowing leaves, wilting, cut stem oozes creamy bacterial slime` |
| **Expected Result** | - Step 1: Rule triggered for Banana Xanthomonas Wilt (BXW).<br>- Matched symptoms: all entered.<br>- Fact: "Results in up to 100 percent loss."<br>- Multi‑step reasoning: generic.<br>- Final conclusion: "The most likely disease is: Banana Xanthomonas Wilt (BXW)". |
| **Actual Result** | As per screenshot. |
| **Status**      | Pass |