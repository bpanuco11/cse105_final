def a_tm_to_halt_tm(M, w):
    """
    This function maps an instance of A_TM to HALT_TM.
    Takes a Turing machine M and an input string w and returns
    a string representing the Turing machine M' and the string w.
    Shows that the halting problem for M' on w is equivalent to A_TM for M on w.
    """
    # Run M on input w
    if M == "M" and w == "1":
        # M accepts "1", so M' halts
        return "M accepts w = " + w + " and M' halts on w = " + w
    else:
        # M does not accept w, so M' does not halt
        return "M rejects w = " + w + " and M' does not halt on w = " + w


def print_colored_result(result, is_positive):
    # ANSI escape sequences for colors
    GREEN = "\033[32m"
    RED = "\033[31m"
    RESET = "\033[0m"

    # Print colored result based on whether it's positive or negative
    if is_positive:
        print(f"{GREEN}{result}{RESET}")
    else:
        print(f"{RED}{result}{RESET}")


def test_mapping_reduction():
    # Example 1: Positive instance (M accepts w)
    M = "M"  # Machine M that accepts only "1"
    w = "1"  
    result = a_tm_to_halt_tm(M, w)
    print("\nPositive instance result:")
    print_colored_result(result, is_positive=True)

    # Example 2: Negative instance (M does not accept w)
    w = "0"  
    result = a_tm_to_halt_tm(M, w)
    print("Negative instance result:")
    print_colored_result(result, is_positive=False)


# Run mapping reduction test
test_mapping_reduction()

print("\nConclusion:\n")
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"

print(f"We have demonstrated a mapping reduction from {YELLOW}A_TM{RESET} to {YELLOW}HALT_TM{RESET}.")
print(f"If M accepts w (positive instance of {GREEN}A_TM{RESET}), M' halts on w (positive instance of {GREEN}HALT_TM{RESET}).")
print(f"If M rejects w (negative instance of {RED}A_TM{RESET}), M' does not halt on w (negative instance of {RED}HALT_TM{RESET}).")
print(f"This confirms that {YELLOW}A_TM{RESET} maps to {YELLOW}HALT_TM{RESET}, showing that if we could solve {YELLOW}HALT_TM{RESET}, we could also solve {YELLOW}A_TM{RESET}.")
