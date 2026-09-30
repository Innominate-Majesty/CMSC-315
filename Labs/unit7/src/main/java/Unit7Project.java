import java.util.Arrays;

/**
 * Unit7Project
 *
 * Price sorter tool that demonstrates bubble sort and selection sort.
 *
 * You will practice:
 * - Sorting arrays of product prices
 * - Comparing sorting algorithms
 * - Swapping array values
 * - Testing sorted output with JUnit
 */

public class Unit7Project {

    public void bubbleSort(int[] prices) {

        // TODO 1: Store the length of the prices array

        // stores the number of elements in the prices array
        int n = prices.length;

        // TODO 2: Use nested loops to compare neighboring prices

        // for loop: passes through the array so each price can move into its correct position
        for (int i = 0; i < n - 1; i++) {

            // boolean to track swap (starts with false because no swap has happened)
            boolean swapped = false;

            // another for loop to compare each neighboring pair that has not already been sorted
            for (int j = 0; j < n - i - 1; j++) {

                // check if the price on the left is greater than the price on the right (left > right)
                if (prices[j] > prices[j + 1]) {

                    // TODO 3: Swap prices when the left value is greater than the right value

                    // temporarily stores the left price so it's not lost
                    int temp = prices[j];

                    // move the right price to the left position
                    prices[j] = prices[j + 1];

                    // move back the original left price into the right position
                    prices[ j + 1] = temp;

                    // record that a swap was made
                    swapped = true;

                }
            }

            // TODO 4: Stop early if no swaps occur during a full pass

            // check if the entire pass finished without making a swap
            if (!swapped) {

                // break
                break;
            }
        }
    }

    public void selectionSort(int[] prices) {

        // TODO 5: Use selection sort to find the lowest remaining price
        // and move it into the correct position

        // for loop: move through each position into the array except the last one
        for (int i = 0; i < prices.length - 1; i++) {

            // make the current position as the lowest price
            int minIndex = i;

            // for loop: search the rest of the array for a lower price
            for (int j = i + 1; j < prices.length; j++) {

                // check if the current price is lower than the lowest price that's been found so far (minIndex)
                if (prices[j] < prices[minIndex]) {

                    // store the new lowest price
                    minIndex = j;

                }
            }

            // temporarily store the price at the current position
            int temp = prices[i];

            // move the lowest remaining price into the current position
            prices[i] = prices[minIndex];

            // move the original current price into the position where the lowest price was found
            prices[minIndex] = temp;

        }
    }

    public int findLowestPrice(int[] prices) {

        // TODO 6: Return the lowest price in the array
        // If the array is empty, return -1

        // check if the array is empty
        if (prices.length == 0) {

            // return -1 becasue it's empty
            return -1;

        }

        // make the first price in the array as the lowest
        int lowest = prices[0];

        // for loop: move through the remaining prices in the array
        for (int i = 1; i < prices.length; i++) {

            // checks if the current price is lower than the stored lowest price (lowest)
            if (prices[i] < lowest) {

                // update the lowest price to the current price
                lowest = prices[i];

            }
        }

        // return the lowest price found in the array
        return lowest;

    }

    public int findHighestPrice(int[] prices) {

        // TODO 7: Return the highest price in the array
        // If the array is empty, return -1

        // check if the array is empty
        if (prices.length == 0) {

            // return -1
            return -1;

        }

        // make the first price in the array as the highest
        int highest = prices[0];

        // for loop: move through the remaining prices in the array
        for (int i = 1; i < prices.length; i++) {

            // checks if the current price is higher than the stored highest price (highest)
            if (prices[i] > highest) {

                // update the highest price to the current price
                highest = prices[i];

            }
        }

        // return the highest price found in the array
        return highest;

    }

    public static void main(String[] args) {

        Unit7Project app = new Unit7Project();

        int[] prices = {42, 19, 88, 7, 31};
        app.bubbleSort(prices);
        System.out.println("Bubble sorted prices: " + Arrays.toString(prices));

        int[] morePrices = {42, 19, 88, 7, 31};
        app.selectionSort(morePrices);
        System.out.println("Selection sorted prices: " + Arrays.toString(morePrices));
    }
}