<script>
    let question = "";
    let answers = ["1", "2", "3", "4"];
    let answers_obj = [];
    let answers_points = [0, 0, 0, 0];
    let points_blu;
    let points_red;
    let pool;
    let exes;
    let fetched = false;
    // once every .5 second, refresh
    setInterval(() => {
        fetch_data();
    }, 500);

    function fetch_data() {
        fetch("http://127.0.0.1:8000/")
            .then((response) => response.json())
            .then((data) => {
                fetched = true;
                question = data.question;
                answers = data.answers;
                answers_points = data.answers_points;
                points_blu = data.points_blu;
                points_red = data.points_red;
                exes = data.exes;
                pool = data.pula;
                // combine answers and answers_points into an array of objects
                answers_obj = answers.map((answer, index) => {
                    return {
                        answer: answer,
                        points: answers_points[index],
                    };
                });
            })
            .catch((error) => console.error("Error:", error));
    }
</script>

<main>
    <div class="main">
        {#if fetched}
            <div class="answers">
                <p>
                    <span class="h1">{question}</span>
                    {#if pool > 0}
                        <span class="points super">{pool}</span>
                    {:else}
                        <span class="points super">-</span>
                    {/if}
                </p>
                {#each answers_obj as answer}
                    <p>
                        {answer.answer}
                        {#if answer.points > 0}
                            <span class="points">{answer.points}</span>
                        {:else}
                            <span class="points">-</span>
                        {/if}
                    </p>
                {/each}
            </div>
        {/if}
    </div>
</main>
<div class="exes pointer">
    {#if exes == 1}
        <p><span>X</span> X X</p>
    {:else if exes == 2}
        <p><span>X X </span> X</p>
    {:else if exes == 3}
        <p><span>X X X</span></p>
    {:else}
        <p>X X X</p>
    {/if}
</div>
<div class="red pointer">{points_red}</div>
<div class="blu pointer">{points_blu}</div>

<style>
    @import url("https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap");
    @import url("https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap");
    .super {
        font-size: 100px !important;
    }
    .h1 {
        font-size: 40px;
        max-width: 80%;
        font-style: italic;
        font-weight: 700;
    }
    .pointer {
        position: absolute;
        font-family: "Roboto", sans-serif;
        font-weight: 400;
        color: #1e1e1e;
        font-style: normal;
        font-size: 5rem;
        margin: 0px;
        width: 180px;
        display: flex;
        justify-content: center;
        bottom: 0;
    }
    .red {
        left: 0;
        background-color: rgb(255, 128, 128);
    }
    .blu {
        right: 0;
        background-color: rgb(128, 158, 255);
    }
    .exes {
        left: 50%;
        transform: translateX(-50%);
        color: rgb(87, 87, 87);
        font-size: 5rem;
        font-family: "Roboto Mono", sans-serif;
        display: flex;
        justify-content: center;
        flex-direction: row;
        width: fit-content;
    }
    .exes p {
        margin: 0;
        padding: 0;
        justify-content: center;
        align-items: center;
    }
    .exes span {
        color: white !important;
    }
    .main {
        position: absolute;
        top: 0;
        left: 180px;
        width: calc(100% - 360px);
        height: calc(100% - 5rem);
        margin-top: 5rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: #1e1e1e;
    }
    main {
        position: absolute;
        right: 0;
        background-color: #1e1e1e;
        top: 0;
        width: 100%;
        height: 100%;
    }
    .answers {
        display: flex;
        flex-direction: column;
        font-family: "Roboto Mono", sans-serif;
        font-weight: 400;
        color: white;
        font-style: normal;
        width: 100%;
        justify-content: center;
        align-items: center;
    }
    .answers p {
        margin: 0;
        padding: 0;
        font-size: 4rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }
    .points {
        margin-left: 20px;
        font-size: 50px;
        color: rgb(128, 255, 128);
    }
</style>
