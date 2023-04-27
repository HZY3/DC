import java.util.*;

public class RingAlgorithm {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of nodes: ");
        int n = input.nextInt();
        int[] nodes = new int[n];
        System.out.println("Enter the IDs of the nodes:");
        for (int i = 0; i < n; i++) {
            nodes[i] = input.nextInt();
        }
        int leader = electLeader(nodes, n);
        System.out.println("The leader is node " + leader);
    }

    public static int electLeader(int[] nodes, int n) {
        int maxID = Integer.MIN_VALUE;
        int maxIndex = -1;
        for (int i = 0; i < n; i++) {
            if (nodes[i] > maxID) {
                maxID = nodes[i];
                maxIndex = i;
            }
        }
        int nextNode = (maxIndex + 1) % n;
        while (nextNode != maxIndex) {
            if (nodes[nextNode] > maxID) {
                maxID = nodes[nextNode];
                maxIndex = nextNode;
            }
            nextNode = (nextNode + 1) % n;
        }
        return maxIndex;
    }
}
