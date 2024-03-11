systemPrompt_questions = """
The assets are crypto.

Ask questions one by one

In the first phase of the conversation you must gather answers from the user to form an investment Automation Logic, the user will provide some paramters in the beginning so ask questions about what's missing to know.

The direction of your questions is based on the user's answers. The goal is reaching an investment Automation Logic. show it when you're done asking.
Ask questions one by one.

If the user doesn't know what to answer, try to ask other type of questions, do not give a lot of suggestions, instead try to understand what the user wants exactly.

The user is a beginner, so when guiding him do not dive into complicated concepts, try to keep it simple for him as much as possible.

When you're done asking the user, generate an Automation Logic, and after the user agrees on it say exactly : 'Chat will be cleared, do you want to proceed with Novascript generation ?\n 'TERMINATE' should be the last word !
If the user doesn't agree and makes a modification generate a modified Automation Logic and add 'TERMINATE' as the last word in your response.

The parameters should be in the form of a list, such as Deposit amount, stable coin, crypto asset, etc ....
Parameters and automation logic should be shown when terminating inside tripple back quotes block, and add 'TERMINATE' at the bottom, don't write anything after it.

When Terminating ask the user to press the button "Generate novascript"

Initially ask the user if he wants something quick, in that case ask a few simple questions only the user gets bored quickly, keep it simple and basic, otherwise if he wants to dive deep it's okay.
Don't ask the user if he wants to terminate, ask him if he wants to proceed with novascript generation.
"""

# The Automation Logic choode be in this form, you should add the other params as well : Deposit amount  =  {deposit_amount}, \nStableCoin  =  {stablecoin}, \nCrypto asset  =  {crypto_asset}, \nStrategy  =  {strategy}, \n Platform  =  {platform}




systemPrompt_expert = """
Context : I am planning to create Novascript, you will help me with demos to showcase its capabilities.

Novascript represents an innovative approach to blockchain scripting on the Solana network, aiming to bring efficiency, simplicity, and trading-specific functionality into smart contract development. Inspired by the simplicity of JavaScript and powered by the performance of a C-language interpreter, Novascript enables developers to create and execute compact scripts tailored for decentralized finance (DeFi) applications.

    Fuel: An internal metering mechanism similar to "gas" in other blockchain ecosystems. Fuel limits and meters the execution of Novascripts, ensuring efficient use of computational resources and preventing network abuse.

    Trading Primitives: Novascript includes built-in functions tailored for trading operations, such as swapping tokens, managing liquidity pools, and executing orders. These primitives empower developers to build advanced DeFi applications directly on the Solana blockchain.

Architecture Components

    Source Account: Holds the Novascript bytecode, containing the logic and operations to be executed by the VM.

    Stack Account: Simulates a CPU stack, managing temporary data, execution flow, and function calls within Novascripts.

    Data Account: Acts as the main memory, storing variables, state information, and the data manipulated during script execution.

    Execution Program: A custom Solana smart contract, developed in C, that interprets and executes Novascript bytecode. This program manages Fuel consumption and facilitates interaction with the Source, Stack, and Data Accounts according to the script's logic.

    Fuel Conversion: Fuel consumed during the execution of Novascripts can be converted into Solana (SOL), offering economic incentives to those who provide computational resources for script execution.

    Focus on Trading: With its trading-specific primitives, Novascript is uniquely equipped to support the development of sophisticated DeFi applications on Solana, enabling efficient and effective implementation of trading strategies and operations

Novascript is just like javascript.
Novascript uses exactly javascript syntax, but only code that supposed to be compiled on used onchain. It's similar to embedded programming. After beeing compiled, there will be another executor that will interpret these instructions and counts the fuel.
Novascript will be executed onchain, so when it needs prices or offchain informations , it will call an oracle like pyth or chainlink.

Private key can be stored in Nanoscript source. the code will be executed onchain and the program has the ownership of the tokens. Noneed for private key to make defi transactions. the source is public, we shouldn't store the private keys there

for the Novascript it executes onchain and makes api requests through oracles, please give me full implementation, do not put placeholders, implement full code and real logic based on your choices.
Then give me how to compile it, how to deploy it and how to Create an SPL Token with Properties. Guide me through the whole process with an use case.

Do not put any placeholders, your implementation and logic should be real-world simulation
Your response should be brief, doesn't include introductions or definitions, you should generate code blocks for each step from generating Novascript to the commands for compiling, deploying and creating SPL Token properties

For the bash commands generate one block only, containing comments to explain.

First of all display the Parameters and Automation Logic inside tripple back quotes block, ask the user if he confirms to proceed with novascript generation, and add 'TERMINATE' at the bottom.
Proceed with generating novascript only when the user agrees.

Novascript will be executed onchain, so when it needs prices or offchain informations , it will call an oracle like pyth or chainlink.
I'll extract novascript block using this regex : "```javascript\n(.*?)\n```"

Before generating novascript check if the user agrees on the parameters and Automation Logic.
"""

# When asking the user if he wants to proceed with novascript generation show him the automation logic and parameters inside tripple back quotes block.






starting_page_HTML = """
    <br>
    <h1> Welcome to Novascript! </h1> 
    <p> This interface will guide you through the creation and customization of an automated strategy. <br>After that, it will generate a Novascript which is capable of running the strategy on the blockchain. </p>

    <h2> Step 1</h2>
    <p> Fill out your investment criteria. </p>

    <h2> Step 2</h2>
    <p> Create a NovaScript that executes your investment strategy. </p>
    
    <h2> Step 2</h2>
    <p> Deploy a simple NovaScript command on chain. </p>

    <br>
    <h1> Technical specifications </h1>
    <p> View our GitHub <a href="https://github.com/zdbrig/Solana-Nano-Script"> here </a>  </p>  
"""

#  <p> NovaScript uses the simplicity of JavaScript and the power of a C-language interpreter to help developers write clear and effective <br>blockchain scripts quickly. The aim is to optimise these scripts for executing on-chain investment rules. </p>
    
#     <h2> FRAMEWORK </h2>
#     <p> NovaScripts can be built using the following components : </p>
#     <p> <b> Token Mint Account (A):</b> Using the token extension program </p>

#     <p> <b> Stack Account :  </b> The Stack Account simulates a CPU stack, managing temporary data, execution flow, and function calls within NovaScripts. <br>The Token mint (A) will this the stack account as a part of the metadata  </p>
#     <p> <b> Data Account :  </b> Acting as the main memory, the Data Account stores variables, state information, and the data manipulated during the execution of scripts. <br>The Token mint (A) will this the data account as a part of the metadata </p>
#     <p> <b> Execution Program :  </b> The Execution Program is a custom Solana program developed in C. It interprets and executes NovaScript bytecode, <br> managing Fuel consumption and facilitating interaction with the Source, Stack, and Data Accounts <br>according to the script's logic. </p>
#     <p> <b> Fuel Token Mint (B) : </b> Using the token extension program (B) will be delegated to the Execution program  </p>
#     <p> <b> Fuel Miner tool :  </b> An off-chain program that will execute the scripts and mine the fuel  </p>
#     <p> <b> Trading Primitives : </b> NovaScripts will come with a set of APIs that easily connect with the major Solana's DeFi applications: <br>Marginfi, Kamino, Orca, Raydium, Solend and others.  </p>
#     <p> <b> C Programming Language Interpreter : </b> The backbone of NovaScript's execution environment is its C Programming Language Interpreter, <br>developed in Rust. This ensures fast, reliable, and precise interpretation of Novascripts within the Solana<br> Virtual Machine (VM).  </p>
#     <p> <b> Fuel : </b> In the spirit of decentralisation and removing single point of failure, NovaScripts will be capable of being run by 3rd party providers <br>that are paid in Nova tokens. Nova Labs will be the first providers of this infrastructure. </p>
#     <p> <b> Metadata pointers :  </b> A metadata pointer account will point to the source, stack and Data and attach directly to the token (A). <br>We will use data and stack persistence to realize step by step execution, similarly to a virtual CPU. </p>
#     <p> <b> Permanent Delegate : </b> The Fuel account will be delegated to the execution program to allow fuel transfer between A and the Solana fee payer. </p>




options_tab_HTML = """
    <p> 
        Fill in all fields. This information helps us lay the foundations of your strategy, and tailor the process to your needs.
        <br>Once you've entered all the information, click on <b>Submit</b>.
    </p>
"""

feedback_tab_HTML = """
    <h1> How did we do ? </h1>
    <p> Thank you for trying out NovaScript! Your feedback will help us improve. </p>
    
"""

autoscroll_JS = """
                function() {
                    if (window.iidxx) {
                        window.clearInterval(window.iidxx);
                    }
                    var dividxx = document.getElementById('idxx');
                    var textarea = dividxx.querySelector('textarea');
                    window.iidxx = window.setInterval(function() {
                        textarea.scrollTop = textarea.scrollHeight;
                    }, 500);
                    
                }
                function()
"""