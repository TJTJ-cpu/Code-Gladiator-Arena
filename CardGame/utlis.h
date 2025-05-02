#include "cards.h"

inline 
std::vector<Card> CreateDeck(){
    std::vector<Card> deck;
    int suitsCount = static_cast<int>(Suit::Count);
    int rankCount = static_cast<int>(Rank::Count);
    std::cout << "Suit Count: " << suitsCount << std::endl;
    std::cout << "Card Count: " << rankCount<< std::endl;
    int sum = 0;

    for (int i = 0; i < suitsCount; i++){
        for (int j = 0; j < rankCount; j++){
            Card card = Card(Suit(i), Rank(j));
            deck.push_back(card);
        }
    }
    std::cout << "Sum Count: " << sum << std::endl;
    return deck;
}



