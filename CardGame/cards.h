#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <iomanip>

enum class Suit {
    Hearts,
    Diamonds,
    Clubs,
    Spades,
    Count
};


enum class Rank {
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    Ten,
    Jack,
    Queen,
    King,
    Ace,
    Count
};


class Card {
private:
    Suit suit;
    Rank rank;

public:
    Card(Suit s, Rank r) : suit(s), rank(r) {}

    Suit getSuit() const { return suit; }
    Rank getRank() const { return rank; }

    std::string 
    toString() const{
        static const std::string suits[] = {"Hearts", "Diamonds", "Clubs", "Spades"};
        static const std::string ranks[] = {
            "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "Jack", "Queen", "King", "Ace"
        };
        std::ostringstream oss;
        oss << std::left << std::setw(6) << ranks[static_cast<int>(rank)]
            << "of " << suits[static_cast<int>(suit)];
        return oss.str();
    }
};

class Deck{

};
