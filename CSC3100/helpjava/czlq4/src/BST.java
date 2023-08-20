import java.util.*;
public class BST {
    class Node {
        int value, size;
        Node left, right;
        long sum;
        Node(int t) {
            size = 1; //the number of node(including the root) in this subtree
            value = t;
            sum = t; // the sum of value of nodenode(including the root) in this subtree
        }
    }

    Node root;
    Node insert(Node node, int key, int value) {
        if (node == null)
            return new Node(value);

        if (node.left != null){
            // nedd to insert in the right subtree
            if (node.left.size < key){
                key -= (node.left.size+1); //update the key relative to the new subtree
                node.right = insert(node.right, key, value);
            }
            // nedd to insert in the left subtree
            else
                node.left = insert(node.left, key, value);
        }
        else{ //left is null
            if (key == 0)
                node.left = new Node(value);
            else{
                key --;
                node.right = insert(node.right, key, value);
            }
        }
        node.sum += value; //update the sum of the root
        node.size ++; //update the size
        return node;
    }

    Node successor(Node node) {
        Node current = node;
        if (current.left == null)
            return node;
        else
            current = successor(current.left);
        return current;
    }

    Node delete(Node node, int key, int value) {
        if (node == null) {
            return null;
        }
        if (node.left != null) {
            if (key <= node.left.size) { //deleted position is in left subtree
                node.sum -= value;
                node.size--;
                node.left = delete(node.left, key, value);
            }
            else if (key > node.left.size+1) { //deleted position is in right subtree
                key -= (node.left.size + 1); //update the key relative to the new subtree
                node.size--;
                node.sum -= value;
                node.right = delete(node.right, key, value);
            } else if (key == node.left.size+1) { // deleted position is the root
                if (node.right == null) {
                    node = node.left;
                } else { // find the successor in the rightchild and replace the value
                    Node temp = successor(node.right);
                    node.size--;
                    node.sum -= node.value;
                    node.value = temp.value;
                    node.right = delete(node.right, 1, temp.value); //since key is the smallest position
                }
            }
        }
        else{ //left is null
            if (key == 1) // deleted position is the root
                return node.right;
            else{ // deleted position is in the right subtree
                key --;
                node.size --;
                node.sum -= value;
                node.right = delete(node.right, key, value);
            }
        }
        return node;
    }
    Node search(Node node, int key){
        Node current = node;
        if (current.left != null) {
            if (current.left.size == key - 1)
                return current;
            else if (current.left.size >= key) {
                return search(current.left, key);
            } else
                key -= (current.left.size + 1);
                return search(current.right, key);
        }
        else{
            if (key == 1)
                return current;
            else
                return search(current.right, key-1);
        }
    }

    long searchSum(Node node, int pos){
        long ans = 0;
        if ((node.left!=null)&&(pos > 0)) {
            if (node.left.size == pos)
                return node.left.sum;
            else if (node.left.size >= pos)
                ans = searchSum(node.left, pos);
            else {
                pos -= (node.left.size + 1);
                if (node.right!=null)
                    ans += (node.value + node.left.sum + searchSum(node.right, pos));
                else
                    ans += (node.value + node.left.sum);
            }
        }
        else{
            if (pos == 1){
                return node.value;
            } else if (pos == 0) {
                return 0;
            } else{
                ans += (node.value + searchSum(node.right, --pos));
            }
        }
        return ans;
    }
    long sum(Node root, int l, int r){
        long sumLeft = 0;
        if (l > 1){sumLeft = searchSum(root, l-1);}
        long sumRight = searchSum(root, r);
        return sumRight-sumLeft;
    }

    public static void main(String[] args) {
        BST tree = new BST();
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        for (int i = 0; i < num; i++) {
            int type_operation = scan.nextInt();
            if (type_operation == 1) {
                int pos = scan.nextInt();
                int value = scan.nextInt();
                tree.root = tree.insert(tree.root, pos, value);
            }
            if (type_operation == 2) {
                int pos = scan.nextInt();
                int value = tree.search(tree.root, pos).value;
                tree.root = tree.delete(tree.root, pos, value);
            }
            if (type_operation == 3) {
                int l = scan.nextInt();
                int r = scan.nextInt();
                long sum = tree.sum(tree.root, l, r);
                System.out.println(sum);
            }
        }
    }
}
