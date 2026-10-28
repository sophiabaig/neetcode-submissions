class Solution {
    public boolean isValid(String s) {

        HashMap<Character, Character> matches = new HashMap<>();
        Deque<Character> stack = new ArrayDeque<>();
        matches.put(')', '(');
        matches.put('}', '{');
        matches.put(']', '[');

        for (int i = 0; i < s.length(); i++) {
            if (!matches.containsKey(s.charAt(i))) {
                stack.push(s.charAt(i));
            }
            else {
                if (!stack.isEmpty() && stack.peek().equals(matches.get(s.charAt(i)))){
                    stack.pop();
                } else {
                    return false;
                }
            }
        }   
        return stack.isEmpty();
    }
}
