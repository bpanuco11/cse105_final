def prologue():
    print("\nLet \033[93mD\033[0m be an automaton that fulfills the requirements for a valid \033[93mDFA\033[0m.\n"
          "Let Language \033[93mL(D)\033[0m = { all strings over \033[93m{a, b}*\033[0m where the substring \033[93m\"aaa\"\033[0m "
          "is not present }.\n")

def run_dfa(dfa, w):
    # Extract DFA components
    states = dfa["states"]
    alphabet = dfa["alphabet"]
    transition_function = dfa["transition_function"]
    start_state = dfa["start_state"]
    accept_states = dfa["accept_states"]
    
    # Validate the input string; return False if invalid
    if not all(char in alphabet for char in w):
        return False  
    
    # Start from the start state
    current_state = start_state
    
    # Process each character in the string
    for char in w:
        # Transition to the next state
        current_state = transition_function[current_state][char]
    
    # Check if the final state is an accept state
    return current_state in accept_states

# Language L(D) = { all strings over {a, b}* where substring "aaa" is not present }
dfa = {
    "states": {"q0", "q1", "q2", "q3"},
    "alphabet": {"a", "b"},
    "transition_function": {
        "q0": {"a": "q1", "b": "q0"},
        "q1": {"a": "q2", "b": "q0"},
        "q2": {"a": "q3", "b": "q0"},
        "q3": {"a": "q3", "b": "q3"}
    },
    "start_state": "q0",
    "accept_states": {"q0", "q1", "q2"}
}

# List of 10 test inputs, first 5 accepted (including empty string) and last 5 rejected (including out of alphabet)
test_inputs = [
    "bbaa",        # Accepted (valid string, accepted by DFA)
    "a",           # Accepted (valid string, accepted by DFA)
    "",            # Accepted (empty string, accepted by DFA)
    "bba",         # Accepted (valid string, accepted by DFA)
    "ab",          # Accepted (valid string, accepted by DFA)
    "bbac",        # Rejected (invalid alphabet 'c')
    "abcd",        # Rejected (invalid alphabet 'd')
    "aaa",         # Rejected (valid input, but doesn't reach an accept state)
    "baaab",       # Rejected (valid input, but doesn't reach an accept state)
    "aaabbb",      # Rejected (valid input, but doesn't reach an accept state)
]

def color_output(result):
    """Return colored output based on True or False result."""
    return "\033[92mTrue\033[0m" if result else "\033[91mFalse\033[0m"

# Prologue with colored text
prologue()

# Test the function with all the test inputs
print('\033[94mTest:\033[0m\n')
for w in test_inputs:
    result = run_dfa(dfa, w)
    colored_result = color_output(result)
    print(f"Input: '{w}' -> {colored_result}")

print("\nBecause we can construct an algorithm that always halts and correctly "
      "determines membership \nfor any \033[93m⟨D, w⟩\033[0m in \033[93mA_DFA\033[0m, we conclude that \033[93mA_DFA\033[0m is \033[92mdecidable\033[0m.")
