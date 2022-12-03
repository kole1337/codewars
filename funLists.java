import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
class Solution {
  static TreeNode flatten(ListNode head) {
    if(head == null)
      return null;
      
    List<Integer> arr = new ArrayList<>();
    getNums(head, arr);
    Collections.sort(arr);
    
    return makeTree(arr, 0);
  }
  
  public static TreeNode makeTree(List<Integer> arr, int i){
    if(i >= arr.size())
      return null;
    return new TreeNode(arr.get(i), makeTree(arr, i * 2 + 1), makeTree(arr, i * 2 + 2));
  }
  public static void getNums(ListNode list, List<Integer> arr){
    if(list != null){
      getNums(list.data, arr);
      getNums(list.next, arr);
    }
  }
  public static void getNums(TreeNode tree, List<Integer> arr){
    if(tree != null){
      if(!arr.contains(tree.value))
         arr.add(tree.value);
      getNums(tree.left, arr);
      getNums(tree.right, arr);
    }
  }
  
}
//https://www.codewars.com/kata/5866ce53dbca9af9940000d3/train/javascript