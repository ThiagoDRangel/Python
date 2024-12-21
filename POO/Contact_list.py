from typing import List


class Contact:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
    
    def __str__(self):
        return f"{self.name} - {self.email}"


class ContactList:
    def __init__(self):
        self.contacts: List[Contact] = []
        self.favorites: List[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        self.contacts.append(contact)

    def _find_contact(self, name: str, from_favorites=False) -> Contact:
        contact_list = self.favorites if from_favorites else self.contacts

        try:
            contact = [c for c in contact_list if c.name == name][0]
        except IndexError:
            raise LookupError(f"Contact named {name} not found")

        return contact

    def remove_contact(self, name: str) -> Contact:
        contact = self._find_contact(name)
        self.contacts.remove(contact)
        return contact

    def add_to_favorites(self, name: str) -> None:
        contact = self._find_contact(name)
        self.contacts.remove(contact)
        self.favorites.append(contact)

    def remove_from_favorites(self, name: str) -> None:
        contact = self._find_contact(name, from_favorites=True)
        self.favorites.remove(contact)
        self.contacts.append(contact)
    
    def __str__(self):
        contacts_str = ", ".join([str(contact) for contact in self.contacts])
        return f"Contacts: {contacts_str}"


# Exemplo de uso
new_contact = Contact("Jorge", "jorge@example.com")
agenda = ContactList()
agenda.add_contact(new_contact)
print(agenda)  # Saída: Contacts: Jorge - jorge@example.com
