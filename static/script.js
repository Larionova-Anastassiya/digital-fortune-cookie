const openButton =
    document.getElementById("open-button");

const anotherButton =
    document.getElementById("another-button");

const initialState =
    document.getElementById("initial-state");

const result =
    document.getElementById("result");

const fortuneText =
    document.getElementById("fortune-text");

const fortuneId =
    document.getElementById("fortune-id");

const cookie =
    document.getElementById("cookie");


async function openFortune() {
    cookie.classList.remove("opening");

    void cookie.offsetWidth;

    cookie.classList.add("opening");

    try {
        const response =
            await fetch("/api/fortune");

        if (!response.ok) {
            throw new Error(
                "Could not retrieve fortune."
            );
        }

        const data =
            await response.json();

        setTimeout(() => {
            fortuneText.textContent =
                `"${data.fortune}"`;

            fortuneId.textContent =
                `FORTUNE #${data.id}`;

            initialState.classList.add(
                "hidden"
            );

            result.classList.remove(
                "hidden"
            );
        }, 350);

    } catch (error) {
        fortuneText.textContent =
            "The future is temporarily unavailable.";

        fortuneId.textContent =
            "PLEASE TRY AGAIN";

        initialState.classList.add(
            "hidden"
        );

        result.classList.remove(
            "hidden"
        );
    }
}


openButton.addEventListener(
    "click",
    openFortune
);


anotherButton.addEventListener(
    "click",
    openFortune
);