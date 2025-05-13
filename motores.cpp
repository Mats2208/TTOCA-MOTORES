
#include <iostream>
#include <utility>
#include "queue.h"
using namespace std;
class Turno {
private:
    string name;

public:
    Turno() {
        name = " ";
    }
    explicit Turno(string n) {
        name = std::move(n);
    }
    void setName(string n) {
        name = std::move(n);
    }
    [[nodiscard]] string getName() const{
        return name;
    }

    friend ostream& operator<<(ostream& os, const Turno& t) {
        os << " Nombre : " << t.name << endl;
        return os;
    }
};

class ColaTurnos {
private:
    Queue<Turno> cola;

public:
    void agregarTurno(const Turno &t) {
        cola.push(t);
        cout << "turno agragado : " << t << endl;
    }
    void atenderTurno() {
        Turno t;
        if (cola.pop(t)) {
            cout << "atendiendo : " << t << endl;
        }else {
            cout << "no hay turnos por atender : " << endl;
        }
    }
    void verTurno()const {
        Turno t;
        if (cola.peek(t)) {
            cout << "turno actual : " << t << endl;
        }else {
            cout << "no hay turnos esperando : " << endl;
        }
    }
    void mostrar() const{
        cout << "cola actual : " << endl;
        cola.print();
    }
    [[nodiscard]] bool estaVacia() const {
        return cola.isEmpty();
    }

    [[nodiscard]] int cantidadTurnos() const {
        return cola.getSize();
    }
};
