// 150. Evaluate Reverse Polish Notation
// https://leetcode.com/problems/evaluate-reverse-polish-notation/

import java.util.Set;
import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> stack = new Stack<>();

        Set<String> operators = Set.of("+", "-", "*", "/");

        for (String token : tokens) {
            if (operators.contains(token)) {
                int second = Integer.parseInt(stack.pop());
                int first = Integer.parseInt(stack.pop());

                int result = 0;

                switch (token) {
                    case "+":
                        result = first + second;
                        break;

                    case "-":
                        result = first - second;
                        break;

                    case "*":
                        result = first * second;
                        break;

                    case "/":
                        result = first / second;
                        break;
                }
                stack.add(Integer.toString(result));
            } else {
                stack.add(token);
            }
        }

        return Integer.parseInt(stack.pop());
    }
}

/*
 * tokens = ["2","1","+","3","*"]
 * ((2 + 1) * 3) = 9
 * 
 * tokens = ["4","13","5","/","+"]
 * (4 + (13 / 5)) = 6
 */