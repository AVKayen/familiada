<script>
    let points_blu_add = 0;
    let points_red_add = 0;
    let points_blu;
    let points_red;

    let question = "";
    let answers = ["1", "2", "3", "4"];
    let answers_points_uncovered = [0, 0, 0, 0];
    let answers_uncovered = ["1", "2", "3", "4"];
    let answers_obj = [];
    let pool;
    let exes;
    let interactWithAPI = (string) => {
        fetch(`http://127.0.0.1:8000/${string}`).catch((error) =>
            console.error("Error:", error),
        );
    };
    let refresh_data = () => {
        fetch("http://127.0.0.1:8000/")
            .then((response) => response.json())
            .then((data) => {
                question = data.question;
                answers = data.answers;
                answers_points_uncovered = data.answers_points_uncovered;
                answers_uncovered = data.answers_uncovered;
                points_blu = data.points_blu;
                points_red = data.points_red;
                exes = data.exes;
                pool = data.pula;
                answers_obj = answers_uncovered.map((answer, index) => {
                    return {
                        answer: answer,
                        answer_uncovered: answers[index],
                        points: answers_points_uncovered[index],
                    };
                });
            })
            .catch((error) => console.error("Error:", error));
    };
    setInterval(() => {
        refresh_data();
    }, 500);
</script>

<h1>Panel kontrolny Familiady "Ochrona Rodzicielska"</h1>
<h2>Sekcja Punktów</h2>
<section>
    <div class="row">
        <input type="number" bind:value={points_blu_add} />
        <button on:click={() => interactWithAPI(`addpoints/blu/${points_blu_add}`)}>Dodaj punkty niebieskie</button>
    </div>
    <div class="row">
        <input type="number" bind:value={points_red_add} />
        <button on:click={() => interactWithAPI(`addpoints/red/${points_red_add}`)}>Dodaj punkty czerwone</button>
    </div>
    <div class="row">
        <p>Punkty niebieskie: {points_blu}</p>
        <p>Punkty czerwone: {points_red}</p>
    </div>
</section>
<h2>Sekcja Pytań</h2>
<h3>Pytanie:</h3>
{question} <br />
<button on:click={() => interactWithAPI(`uncover_all`)}>Otwórz wszystkie</button> 
<button on:click={() => interactWithAPI(`next_q`)}>Następne Pytanie</button> <br />
<h3>Pula:</h3>
{pool}
<button on:click={() => interactWithAPI(`addpoints/blu/${pool}`)}>Dodaj do niebieskich</button>
<button on:click={() => interactWithAPI(`addpoints/red/${pool}`)}>Dodaj do czerwonych</button>

<br />
<h3>X'y:</h3>
{exes} 
<button on:click={() => interactWithAPI(`exes/add`)}>Dodaj X</button>
<button on:click={() => interactWithAPI(`exes/reset`)}>Resetuj X</button>
<br />

<main>
    <div class="main">
        <div class="answers">
            {#each answers_obj as answer, i}
                <p>
                    {answer.answer}, <i>{answer.answer_uncovered}</i>
                    <button on:click={() => interactWithAPI(`uncover/${i + 1}`)}>
                        <span class="points">{answer.points}</span>
                    </button>
                </p>
            {/each}
        </div>
    </div>
</main>

<style>
    @import url("https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap");
    @import url("https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap");

    section {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .row {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
    }
    .row p,
    .row button {
        margin: 10px;
        padding: 2px;
    }
    h1,
    h2 {
        font-family: "Roboto", sans-serif;
        font-weight: 800;
    }
    h3 {
        all: unset;
        font-size: 1.3rem;
        font-family: "Roboto", sans-serif;
        font-weight: 600;
    }
    .answers {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
    }
</style>
