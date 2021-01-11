# TODO
# Lots of things.
# We need to create a server to receive and process these votes (add voting record to db, logging, verification etc)
# We need to attach a signature of the sent data to make sure the data is not altered during transfer
# Pimp the TKinter GUI
# Cleanup this code lol


from tkinter import *
from tkinter import messagebox
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

root = Tk()  # Instantiate main tkinter window.


class VoteObject:  # class for vote records
    def __init__(self, vote_id, vote_record, name):
        self.name = name
        self.vote_id = vote_id
        self.vote_record = vote_record

    def __repr__(self):
        return self.vote_id

    def encrypt_vote_record(self):
        self.name = encrypt_with_public(self.name)
        self.vote_id = encrypt_with_public(self.vote_id)
        self.vote_record = encrypt_with_public(self.vote_record)
        print(self.vote_record)


def quit_tkinter():
    root.destroy()


def encrypt_with_public(str):
    recipient_key = RSA.import_key(open("keys/frans_rsa_key.pem").read())
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    print(cipher_rsa)
    return cipher_rsa.encrypt(str.encode())


def construct_vote():  # Create voting struct
    if vote_name.get() and vote_id_record.get() != "" and vote_option_var.get() != 'Selecteer een kandidaat':
        return VoteObject(name=vote_name.get(), vote_id=vote_id_record.get(), vote_record=vote_option_var.get())
    else:
        messagebox.showerror(title="You have not filled out all fields!",
                             message="Please check your input fields there are some missing values.".format( ))
        return False


def create_vote_package():  # Encrypt voting object for transmission encrypt with public key of the server
    try:
        vote = construct_vote()
        print(f"A new vote was cast;\n Name: {vote.name}\n vote_identifier: {vote.vote_id}\n"
              f" vote_decision: {vote.vote_record}\n")
        vote.encrypt_vote_record()

        print(f"A new encrypted vote was recorded ;\n Name: {vote.name}\n vote_identifier: {vote.vote_id}\n"
              f" vote_decision: {vote.vote_record}\n")
    except AttributeError:
        pass


# Voter name tkinter logic
vote_name_label = Label(root, text="Name: ")
vote_name_label.grid(row=0, column=0)
vote_name = StringVar()  # Variable for saving the vote decision
vote_name_entry_box = Entry(root, textvariable=vote_name)  # Tkinter entry-box for the vote
vote_name_entry_box.grid(row=0, column=1)

# Voter identifier tkinter logic
vote_id_label = Label(root, text="Unique identifier: ")
vote_id_label.grid(row=1, column=0)
vote_id_record = StringVar()  # Variable for saving a voters unique identifier
vote_id_entry_box = Entry(root, textvariable=vote_id_record)  # Tkinter entry-box for the vote
vote_id_entry_box.grid(row=1, column=1)

# Voter record tkinter logic
vote_details_label = Label(root, text="Vote decision: ")
vote_details_label.grid(row=2, column=0)
vote_option_var = StringVar(root)
vote_option_var.set("Selecteer een kandidaat")

w = OptionMenu(root, vote_option_var, "Donald Trump", "Hill Dawg")
w.grid(row=2, column=1)

# Submit button tkinter logic
submit_button = Button(root,  text="Submit vote", command=create_vote_package)  # Submit button to trigger vote_creation
submit_button.grid(row=3, column=1)

# Exit button tkinter logic
exit_button = Button(root,  text="Exit", command=quit_tkinter)  # Exit button to trigger tkinter.destroy
exit_button.grid(row=3, column=0)


mainloop()
