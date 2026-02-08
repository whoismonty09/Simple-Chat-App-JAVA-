import java.util.ArrayList;
import java.util.Scanner;

class Message {
    String sender;
    String text;

    Message(String sender, String text) {
        this.sender = sender;
        this.text = text;
    }

    void displayMessage() {
        System.out.println(sender + ": " + text);
    }
}

public class Main {

    static ArrayList<Message> chat = new ArrayList<>();
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        int choice;

        do {
            System.out.println("\n💬 Chat Application developed by Monty");
            System.out.println("1. Send Message");
            System.out.println("2. View Chat History");
            System.out.println("3. Exit");

            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    sendMessage();
                    break;
                case 2:
                    viewChat();
                    break;
                case 3:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice!");
            }

        } while (choice != 3);
    }

    static void sendMessage() {
        System.out.print("Enter your name: ");
        String sender = scanner.nextLine();

        System.out.print("Enter message: ");
        String text = scanner.nextLine();

        chat.add(new Message(sender, text));
        System.out.println("✅ Message sent!");
    }

    static void viewChat() {
        if (chat.isEmpty()) {
            System.out.println("No messages yet.");
        } else {
            System.out.println("\n📜 Chat History:");
            for (Message m : chat) {
                m.displayMessage();
            }
        }
    }
}
