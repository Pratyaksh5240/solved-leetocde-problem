class Solution {
    public String toLowerCase(String s) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char temp = s.charAt(i);

            if (temp >= 'A' && temp <= 'Z') {
                temp = (char)(temp + 32);
            }

            sb.append(temp);
        }

        return sb.toString();
    }
}