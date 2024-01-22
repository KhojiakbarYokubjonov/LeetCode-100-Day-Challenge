class Solution {
    public String longestPalindrome(String s) {
        int start = 0; int end = 0;
        int N = s.length();
        for(int i=0; i<N; i++){
            int[] ind1 = longestPal(i, i, N, s);
            if ((ind1[1] - ind1[0]) > (end - start)) {
                start = ind1[0];
                end = ind1[1];
            }
            int[] ind2 = longestPal(i, i+1, N, s);
            if (ind2[1] - ind2[0] > (end - start)) {
                start = ind2[0];
                end = ind2[1];
            }
        }
        return s.substring(start, end);
        
    }
    
    
    private int[] longestPal(int l, int r, int N, String s) {
        while(l >= 0 && r < N) {
            if (s.charAt(l) != s.charAt(r)) { break;}
            l--;
            r++;
        }
        return new int[] {l+1, r};
    }
}