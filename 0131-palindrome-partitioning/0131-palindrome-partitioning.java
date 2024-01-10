class Solution {
     List<List<String>> res;
     List<String> temp;
    public List<List<String>> partition(String s) {
        res = new ArrayList<List<String>>();
        temp = new ArrayList<>();
        
        dfs(0, s);
        
        return res;
        
    }
    
    private void dfs(int start, String s) {
        System.out.println("start index " + start);
        if(start >= s.length()){ res.add(new ArrayList(temp));}
        
        for(int i=start; i < s.length(); i++) {
            if(isPali(s, start, i)) {
                System.out.println("found " + s.substring(start, i+1));
                temp.add(s.substring(start, i+1));
                dfs(i+1, s);
                temp.remove(temp.size()-1);
            }
        }
    }
    
    private boolean isPali(String s, int l, int r) {
        if (s.length() == 1) return true;
        while (l < r) {
            if(s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}