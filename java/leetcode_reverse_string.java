// https://leetcode.com/submissions/detail/671327354/
// https://leetcode.com/problems/reverse-string/discuss/1901903/java-two-pointers-easy-know-your-loops-explained
class Solution {
    public void reverseString(char[] s) {
        for(int head = 0, tail = s.length-1; head < tail; head++, tail--)
        {
            char temp = s[head];
            s[head] = s[tail];
            s[tail] = temp;
        }
    }
}
// Runtime: 0 ms, faster than 100.00% of Java online submissions for Reverse String.
// Memory Usage: 48.9 MB, less than 94.07% of Java online submissions for Reverse String.

// class Solution {
//     public void reverseString(char[] s) {
//         int head = 0;
//         int tail = s.length - 1;
//         char temp;

//         do{
//             temp = s[head];
//             s[head] = s[tail];
//             s[tail] = temp;
//             head++;
//             tail--;
//         }while (head < tail);
//     }
// }
// Runtime: 0 ms, faster than 100.00% of Java online submissions for Reverse String.
// Memory Usage: 49.3 MB, less than 84.59% of Java online submissions for Reverse String.


// class Solution {
//     public void reverseString(char[] s) {
//         int head = 0;
//         int tail = s.length - 1;
//         // char temp;

//         while (head < tail)
//         {
//             char temp = s[head];
//             s[head] = s[tail];
//             s[tail] = temp;
//             head++;
//             tail--;
//         }
//     }
// }
//    Runtime: 0 ms, faster than 100.00% of Java online submissions for Reverse String.
// Memory Usage: 49 MB, less than 91.61% of Java online submissions for Reverse String.