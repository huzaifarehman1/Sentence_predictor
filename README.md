# Sentence_predictor
This project uses higer order markov chain to build a ai system that writes like the person text that it recieved as input

# Markov Chain Text Generation 
It reads input text, builds a transition model of words, and then generates new sentences that mimic the style of the source text.  

---

## 🔹 Features
- Uses **n-th order Markov Chains** (configurable with `ORDER`).
- Supports punctuation handling (`.` and `,` treated as separate tokens).
- Generates random but structured sentences using **probability distributions** (`torch.distributions.Categorical`).
- Cleans input text automatically (keeps only alphanumeric, spaces, `.` and `,`).
- Pretty-prints generated sentences in a numbered format.

---

## 🔹 How It Works
1. **Input Text**  
   - Provide a file path in `path_input.txt`.  
   - Example:  
     ```
     /home/username/data/input.txt
     ```
   - The program reads the content of this file as training data.  

2. **Data Filtering**  
   - Converts to lowercase.  
   - Removes unwanted symbols.  
   - Splits punctuation (`,` and `.`) into separate tokens.  

3. **Transition Model**  
   - Creates a dictionary mapping from `(previous N words)` → `(next word probability distribution)`.  
   - Uses **Markov Chains** to generate text based on this model.  

4. **Sentence Generation**  
   - Picks random starting sequences (after `.`).  
   - Samples next words using categorical probability.  
   - Stops when the requested number of sentences is generated.  