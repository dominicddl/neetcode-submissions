class Solution {
    public String encode(List<String> strs) {
        StringBuilder builder = new StringBuilder();
        for (String str : strs) {
            builder.append(Base64.getEncoder().encodeToString(str.getBytes())).append('#');
        }
        return builder.toString();
    }   

    public List<String> decode(String str) {
        List<String> output = new ArrayList<>();
        int i = 0;
        StringBuilder token = new StringBuilder();
        while (i < str.length()) {
            char c = str.charAt(i);
            if (c == '#') {
            byte[] decodedBytes = Base64.getDecoder().decode(token.toString());
            output.add(new String(decodedBytes));
            token.setLength(0);
            } else {
                token.append(c);
            }
            i++;
        }
        return output;
    }
}
