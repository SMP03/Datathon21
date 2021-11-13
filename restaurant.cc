#include <iostream>
using namespace std;

int mes_gran(int a, int b){
    if (a >= b) return a;
    else return b;
  }

void mes_gran5(int a, int b, int c, int d, int e, int& f){
  f = mes_gran(a, mes_gran(b, mes_gran(c, mes_gran(d, e))));
  }


void restaurant_type(int a, int& exoticos, int& fofisano, int& f_food, int& upscale, int& bar){
    if (a == 1) ++exoticos, ++fofisano;
    else if (a == 2) ++fofisano, ++upscale;
    else if (a == 3) ++f_food;
    else if (a == 4) ++fofisano;
    else if (a == 5) ++bar;
    else if (a == 6) ++fofisano;
    else if (a == 7) ++fofisano, ++f_food;
    else if (a == 8) ++f_food, ++bar;
    else if (a == 9) ++fofisano;
    else if (a == 10) upscale += 2;
}
void price_range(int b, int& exoticos, int& fofisano, int& f_food, int& upscale, int& bar){
    if (b == 1) ++f_food, ++bar;
    else if (b == 2) ++fofisano, ++exoticos;
    else if (b == 3) ++upscale;
}

int main(){
    int exoticos = 0;
    int f_food = 0;
    int fofisano = 0;
    int upscale = 0;
    int bar = 0;
    cout << "Choose the type of restaurant you like the most:" << endl << "1. Japanese" << endl << "2. Italian"<< endl << "3. Fast food"<< endl <<  "4. Buffet"<< endl <<  "5. Café"<< endl << "6. Family style"<< endl << "7. American"<< endl <<  "8. Food truck"<< endl << "9. Casual dining" << endl << "10. Restaurantes caros" << endl;
    int a, f;
    cin >> a;
    restaurant_type(a, exoticos, f_food, fofisano, upscale, bar);
    cout << "Choose a suitable price range for you (price for 1 person)" << endl << "1. 5-10 €" << endl << "2. 10-25 €" << endl << "3. +25 €" << endl;
    int b;
    cin >> b;
    price_range(b, exoticos, f_food, fofisano, upscale, bar);
    mes_gran5(exoticos, f_food, fofisano, upscale, bar, f);
     if (f == exoticos){
         cout << "El Xalet de Montjuïc, Av. Miramar 31, 08038 Barcelona España"<< endl << "Zenith Brunch & Cocktails, Gran Via de les Corts Catalanes, 633, 08010 Barcelona España"<< endl << "Gran Viana, Carrer Dels Escudellers 24, 08002 Barcelona España" << endl;
       } else if (f == f_food){
         cout << "Conesa Entrepans, Carrer de La Llibreteria, 1, 08002 Barcelona España" << endl << "Güelly sandwichpark, Av. Coll del portell 77, 08024 Barcelona España" << endl << "La Trocadero, Marina 269, 08025 Barcelona España" << endl << "Maoz, Carrer de Ferrán, 13, 08002 Barcelona España" << endl << "The Fresh Poke Diagonal, Avenida Diagonal, 357 A dos calles de Paseo de Gracia, 08037 Barcelona España" << endl;
       }
       else if (f == fofisano){
         cout << "Don Kilo Gourmet, Carrer Corsega 398, 08037 Barcelona España "<< endl << "Pizzeria Da Nanni Barcelona, Calle Llibreteria 10, 08002 Barcelona España" << endl <<"Casa Amàlia 1950, Passatge Mercat 4, 08009 Barcelona España" << endl << "Big Al's American Kitchen, Corsega 178, 08036 Barcelona España" << endl << "Bacoa, Marques de L'Argentera, 1 Bis, 08003 Barcelona España" << endl << "The Burger Maker Halal Barcelona, Vía Laietana, 12 Metro Jaume I, 08013 Barcelona España" << endl;
       }
       else if (f == upscale){
         cout << "Tast-Ller, Calle Viladomat 137, 08002 Barcelona España" << endl << "Disfrutar, Calle Villarroel, 163, 08036 Barcelona "<< endl << "Sato I Tanaka, Bruc, 79, 08009 Barcelona España" << endl << "Santa Rita Experience, Carrer de Veneçuela 16, 08019 Barcelona España" << endl << "Con Gracia, Martinez de la Rosa 8, 08012 Barcelona España "<< endl;
       }
       else if (f == bar){
         cout << "Tino, Carrer De Muntaner 102, 08036 Barcelona" << endl << "The Coffee House Barcelona, Carrer de València, 143, 08011 Barcelona" << endl << "365 Cafe, Carrer De Mallorca 22, 08013 Barcelona" << endl << "Bar Limon Breakfast&Brunch, Plaça de Pau Vila, 13, 08003 Barcelona "<< endl;
       }
     }
