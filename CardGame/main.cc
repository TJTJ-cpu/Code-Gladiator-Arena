#include "cards.h"
#include "utlis.h"

#include <vector>

int main(){
    Card card(Suit::Hearts, Rank::King);
    // std::cout << card.toString() << std::endl;
    std::cout << "Done" << std::endl;

    std::vector<Card> Deck;
    Deck = CreateDeck();
    for (auto i : Deck)
        std::cout << i.toString() << std::endl;
    return 0;
}

