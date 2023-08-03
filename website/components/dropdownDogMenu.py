# dropdown_menu.py

def get_dropdown_menu():
    # Return the HTML code for the dropdown menu
    return """
    <div class="dropdown">
      <button
        class="btn btn-custom-color dropdown-toggle"
        type="button"
        id="dropdownMenuButton"
        data-toggle="dropdown"
        aria-haspopup="true"
        aria-expanded="false"
      >
        Choose a Dog Breed
      </button>
      <div class="dropdown-menu scrollable-menu" aria-labelledby="dropdownMenuButton">
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Pomeranian', '../static/assets/a-pomeranian.png')"
        >
          <img
            src="../static/assets/a-pomeranian.png"
            alt="Pomeranian"
            width="30"
            height="30"
            class="mr-2"
          />
          Pomeranian
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Shiba Inu', '../static/assets/a-shiba.png')"
        >
          <img
            src="../static/assets/a-shiba.png"
            alt="Shiba Inu"
            width="30"
            height="30"
            class="mr-2"
          />
          Shiba Inu
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Shih Tzu', '../static/assets/a-shih-tzu.png')"
        >
          <img
            src="../static/assets/a-shih-tzu.png"
            alt="Shih Tzu"
            width="30"
            height="30"
            class="mr-2"
          />
          Shih Tzu
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Coton', '../static/assets/a-coton.png')"
        >
          <img
            src="../static/assets/a-coton.png"
            alt="Coton"
            width="30"
            height="30"
            class="mr-2"
          />
          Coton
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Pomapoo', '../static/assets/a-poma-poo.png')"
        >
          <img
            src="../static/assets/a-pomeranian.png"
            alt="Pomapoo"
            width="30"
            height="30"
            class="mr-2"
          />
          Pomapoo
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Maltipoo', '../static/assets/a-malti-poo.png')"
        >
          <img
            src="../static/assets/a-malti-poo.png"
            alt="Maltipoo"
            width="30"
            height="30"
            class="mr-2"
          />
          Maltipoo
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('American Bulldog', '../static/assets/a-american-bulldog.png')"
        >
          <img
            src="../static/assets/a-american-bulldog.png"
            alt="American Bulldog"
            width="30"
            height="30"
            class="mr-2"
          />
          American Bulldog
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Jack Russell', '../static/assets/a-jack-russell-terrier.png')"
        >
          <img
            src="../static/assets/a-jack-russell-terrier.png"
            alt="Jack Russell"
            width="30"
            height="30"
            class="mr-2"
          />
          Jack Russell
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Samoyed', '../static/assets/a-samoyed.png')"
        >
          <img
            src="../static/assets/a-samoyed.png"
            alt="Samoyed"
            width="30"
            height="30"
            class="mr-2"
          />
          Samoyed
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Doberman Pinscher', '../static/assets/a-doberman-pinscher.png')"
        >
          <img
            src="../static/assets/a-doberman-pinscher.png"
            alt="Doberman Pinscher"
            width="30"
            height="30"
            class="mr-2"
          />
          Doberman Pinscher
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Welsh Corgi', '../static/assets/a-welsh-corgi.png')"
        >
          <img
            src="../static/assets/a-welsh-corgi.png"
            alt="Welsh Corgi"
            width="30"
            height="30"
            class="mr-2"
          />
          Welsh Corgi
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Bull Terrier', '../static/assets/a-bull-terrier.png')"
        >
          <img
            src="../static/assets/a-bull-terrier.png"
            alt="Bull Terrier"
            width="30"
            height="30"
            class="mr-2"
          />
          Bull Terrier
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Collie Rough', '../static/assets/a-collie-rough.png')"
        >
          <img
            src="../static/assets/a-collie-rough.png"
            alt="Collie Rough"
            width="30"
            height="30"
            class="mr-2"
          />
          Collie Rough
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('White Terrier', '../static/assets/a-white-terrier.png')"
        >
          <img
            src="../static/assets/a-white-terrier.png"
            alt="White Terrier"
            width="30"
            height="30"
            class="mr-2"
          />
          White Terrier
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('French Bulldog', '../static/assets/a-french-bulldog.png')"
        >
          <img
            src="../static/assets/a-french-bulldog.png"
            alt="French Bulldog"
            width="30"
            height="30"
            class="mr-2"
          />
          French Bulldog
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('a-great-dane', '../static/assets/a-great-dane.png')"
        >
          <img
            src="../static/assets/a-great-dane.png"
            alt="Great Dane"
            width="30"
            height="30"
            class="mr-2"
          />
          Great Dane
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Husky', '../static/assets/a-husky.png')"
        >
          <img
            src="../static/assets/a-husky.png"
            alt="Husky"
            width="30"
            height="30"
            class="mr-2"
          />
          Husky
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Basset Hound', '../static/assets/a-basset-hound.png')"
        >
          <img
            src="../static/assets/a-basset-hound.png"
            alt="Basset Hound"
            width="30"
            height="30"
            class="mr-2"
          />
          Basset Hound
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Border Collie', '../static/assets/a-border-collie.png')"
        >
          <img
            src="../static/assets/a-border-collie.png"
            alt="Border Collie"
            width="30"
            height="30"
            class="mr-2"
          />
          Border Collie
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Chihuahua', '../static/assets/a-chihuahua.png')"
        >
          <img
            src="../static/assets/a-chihuahua.png"
            alt="Chihuahua"
            width="30"
            height="30"
            class="mr-2"
          />
          Chihuahua
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('American Foxhound', '../static/assets/a-american-foxhound.png')"
        >
          <img
            src="../static/assets/a-american-foxhound.png"
            alt="American Foxhound"
            width="30"
            height="30"
            class="mr-2"
          />
          American Foxhound
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Dalmatian', '../static/assets/a-dalmatian.png')"
        >
          <img
            src="../static/assets/a-dalmatian.png"
            alt="Dalmatian"
            width="30"
            height="30"
            class="mr-2"
          />
          Dalmatian
        </a>
        <a
          class="dropdown-item"
          href="#"
          onclick="updateButton('Labrador Retriever', '../static/assets/a-labrador-retriever.png')"
        >
          <img
            src="../static/assets/a-labrador-retriever.png"
            alt="Labrador Retriever"
            width="30"
            height="30"
            class="mr-2"
          />
          Labrador Retriever
        </a>
        <!-- Add more dog breeds as needed -->
      </div>
    </div>
    """
