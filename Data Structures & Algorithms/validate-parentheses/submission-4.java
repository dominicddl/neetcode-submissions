class Solution {
    public char reverseChar(char c) {
        switch (c) {
            case ')': 
                c = '('; 
                break;
            case '}':
                c = '{';
                break;
            case ']':
                c = '[';
                break;
        }
        return c;
    }
    public boolean isValid(String s) {
        // Define a stack 
        Stack<Character> brackets = new Stack<>();
        if (s.length() % 2 != 0) {
            return false;
        }
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '{' || c == '[') {
                // Add to the stack
                brackets.push(c);
            } 
            if (c == ')' || c == '}' || c == ']') {
                // Check the top of the stack
                if (brackets.empty()) {
                    brackets.push(c);
                }
                char top = brackets.peek();
                char rev = reverseChar(c);
                if (rev == top) {
                    // Remove the open bracket from the stack
                    brackets.pop();
                } else if (rev != top) {
                    return false;
                }
            }
        }
        return brackets.empty();
    }
}
