import java.util.*;
public class AVLTree {
    class Node {
        int value, key;
        Node left, right;
        long sum;
        Node(int d, int t) {
            key = d;
            value = t;
            sum = t;
        }
    }

    Node root;
    Node add_size_value(Node node, int value){
        if (node != null){
            add_size_value(node.left, value);
            node.key++;
            node.sum += value;
            add_size_value(node.right, value);
        }
        return node;
    }
    Node insert(Node node, int key, int value, long sum) {
        if (node == null) {
            Node nn = new Node(key, value);
            nn.sum = sum;
            return nn;
        }
        if (key <= node.key) {
            node.key ++;
            node.sum += value;
            node.right = add_size_value(node.right, value);
            node.left = insert(node.left, key, value, sum);
        }
        else{
            sum = node.sum + value;
            node.right = insert(node.right, key, value, sum);
        }
        return node;
    }

    Node predecessor(Node node) {
        Node current = node;
        if (current.right == null)
            return node;
        else
            current = predecessor(current.right);
        return current;
    }
    Node del_key_sum(Node node, int value){
        if (node != null) {
            node.left = del_key_sum(node.left, value);
            node.key--;
            node.sum -= value;
            node.right = del_key_sum(node.right, value);
        }
        return node;
    }
    Node deleteNode(Node root, int key, int value) {
        if (root == null) {
            return null;
        }
        if (key < root.key) {
            root.key --;
            root.sum -= value;
            root.right = del_key_sum(root.right,value);
            root.left = deleteNode(root.left, key, value);
        }
        else if (key > root.key) {
            root.right = deleteNode(root.right, key, value);
        }
        else {
            if ((root.left == null) || (root.right == null)){
                if (root.right != null) {
                    root.right = del_key_sum(root.right, value);
                    root = root.right;
                }
                else
                    root = root.left;
            } else {
                Node temp = predecessor(root.left);
                root.key = temp.key;
                root.value = temp.value;
                root.sum = temp.sum;
                root.right = del_key_sum(root.right, value);
                root.left = deleteNode(root.left, temp.key, temp.value);
            }
        }
        return root;
    }
    Node search(Node node, int key){
        Node current = node;
        if (current.key == key)
            return current;
        else if (current.key > key)
            return search(current.left, key);
        else
            return search(current.right, key);
    }
    long searchSum(Node root, int pos){
        long ans;
        if (root.key == pos)
            return root.sum;
        else if (root.key > pos)
            ans = searchSum(root.left, pos);
        else
            ans = searchSum(root.right, pos);
        return ans;
    }
    long sum(Node root, int l, int r){
        long sumLeft = 0;
        if (l > 1){sumLeft = searchSum(root, l-1);}
        long sumRight = searchSum(root, r);
        return sumRight-sumLeft;
    }

    public static void main(String[] args) {
        AVLTree tree = new AVLTree();
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        for (int i = 0; i < num; i++) {
            int type_operation = scan.nextInt();
            if (type_operation == 1) {
                int pos = scan.nextInt();
                int value = scan.nextInt();
                tree.root = tree.insert(tree.root, pos + 1, value, value);
            }
            if (type_operation == 2) {
                int pos = scan.nextInt();
                int value = tree.search(tree.root, pos).value;
                tree.root = tree.deleteNode(tree.root, pos, value);
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
