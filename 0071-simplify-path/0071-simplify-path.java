class Solution {
    public String simplifyPath(String path) {
        ArrayList<String>stack =  new ArrayList<>();
        String current = "";
        path += "/";
        for(int i=0; i<path.length(); i++) {
            if (path.charAt(i) == '/') {

                if(current.equals("..")) {
                    if(stack.size() > 0) {
                        stack.remove(stack.size() - 1);}
                }else if(!current.equals(".") && current.length() != 0) {
                    stack.add(current);    
                }
                current = "";
            }else {
                current += path.charAt(i);
            }
        }
        if(stack.size() == 0) {return "/";}
        
        String output = "";
        for(String dir: stack) {
            output += ("/" + dir);
        }
        return output;
    }
}