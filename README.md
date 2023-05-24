# bac
avancement sur le grand oral

# Data used
--> https://fr.wikipedia.org/wiki/Inverse_modulaire <br>
--> https://repository.root-me.org/Cryptographie/FR%20-%20Cryptanalyse%20de%20RSA.pdf <br>
--> https://www.methodemaths.fr/les_congruences/ <br>
--> https://fr.wikipedia.org/wiki/Logarithme_discret <br>
--> https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character <br>
--> https://fr.wikipedia.org/wiki/Cryptographie <br>
--> https://fr.wikipedia.org/wiki/Décomposition_en_produit_de_facteurs_premiers <br>
--> https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman <br>
--> https://python.doctor/page-tkinter-interface-graphique-python-tutoriel <br>
--> https://fr.wikipedia.org/wiki/Digital_Signature_Algorithm <br>
--> https://fr.wikipedia.org/wiki/Algorithme_LLL <br>
--> https://crypto.stackexchange.com/questions/101439/how-is-diffie-hellman-linked-to-aes <br>

# problematique

comment sécurisé des transferts de données ?<br>
comment sont sécurisé les données sur internet ?<br>
pourquoi la sécurité du web n'est pas infaillible ?<br>
Les protocoles de sécurité du web peuvent-ils être mis à mal ?<br>
Comment les mathématiques permettent de sécurisé les transfert de données ?<br>

# intro

<h4>Depuis le début de son existence l'Homme à toujours cherché a communiquer des informatio de manière privée et lisible uniquement par le destinataire. C'est cette volonté qui à entrainé au file du temps l'invention de méthode de chiffrement de plus en plus sécurisé en passant par des algorithme simple comme le code césar jusqu'au chiffrement RSA.</h4>

# première partie

<h2>Algorithme symétrique</h2>
<p>Un algorithme de chiffrement symétrisue utilise la même clé pour chiffrer et déchiffrer des données, on peut citer l'algorithme AES, DES ou bien encore tripleDES. Un algorithme symétrique doit être utilisé en parallèle d'algorithme d'échange de clés comme celui de diffie hellman pour garantir la non divulgation de la clé de chiffrement/déchiffrement</p>
<h3>échange de clée diffie Hellman</h3>
<p>L'échange de clé diffi hellman permet à deux tiers d'échanger une clé de chiffrement unique de manière sécurisé. Il repose sur le problème du logarithme discret. Considérons Alice et Bob, deux tiers voulant séchanger une clé. Pour cela, les deux se mettent d'accord sur p un nombre premier alétoire et g un nombre aléatoire inférieur à p. Avec ces deux nombres, Alice peut calculer A = g^a (mod p) et Bob B = g^b (mod p), puis avec les deux tiers peuvent s'échanger les valeur pour calculer B^a (mod p) = g^ab (mod p) et A^b (mod p) = g^ab (mod p). Avec cette méthode, Alice et Bob on pus échanger la valeurs g^ab (mod p) de manières sécurisé car un individu possedant p,g,g^b (mod p) et g^a (mod p) (donc aillant intercepté l'achange) ne peut pas déduire a et b et la clé finale. On peut par exemple utiliser cette méthode pour échanger un phrase de chiffrement AES en utilisant une table comme la table ASCII ou hexadécimal.</p>
<h3>Chiffrement AES</h3>
<p>AES est un algorithme basé sur les portes logique XOR, pas intérréssant car pas très maths</p>
<h2>Algorithme asymetrqiue</h2>
<p>Un algorithme asymétrique est un algoithme utilisant deux clés, une pour déchiffrer et une pour chiffrer. Il sont en théorie plus sécurisé que les algorithmes symétrique car la clé de chiffrement ou de déchiffrement n'est jamais rendue publique</p>
<h3>Chiffrement RSA</h3>
<p>Le RSA est algorithme de chiffrement asymétrique créé par Ronald Rivest, Adi Shamir et Leonard Adleman. Il est très utilisé dans les échange de données sur internet et notament dans les transactions bancaires. Cette méthode se base sur deux nombres premiers p et q qui permet d'en déduire un module de chiffrement n = pq, un exposant de chiffrement(clé publique) e tel que pgcd(e,φ(n)) = 1 et e < φ(n) et enfin un éxposant de déchiffr^ement(clé privée) d tel que d*e ≡ 1 (mod φ(n)) ou d ≡ e^-1 (mod φ(n)). La sécurisé de cette algorithme est défini par la taille des deux nombres premiers p et q choisi, plus p et q sont grands plus le temps de calcule pour les déchiffrer sera long. Pour les déchiffrer on parle d'algorithme de compléxité exponentielle donc les risques osnt quasi inéxistant avec des nombres premiers suffisament grand. Les plus grosses menaces de sécurités reste les ordinateurs quantique et la résolution du problème NPC (P=NP). Mais bon, jusqu'a présent nous avons seulement vue comment chiffrer des nombres avec RSA mais commment peut-on chiffrer des phrases ? Et bien c'est très simple, il suffit juste de convertir les lettres a chiffrer avec la table ASCII ou une autre table qui associe des lettres à des nombres unique pour faire un tableau de nombre à partir de la phrase. Puis on peut chiffrer le tableau nombres par nombres. Le destinataire n'aura plus qu'a déchiffrer le tableau de nombre et reconstituer la phrase avec la même table que pour le chiffrement.</p>
<h3>Signature RSA</h3>
<p>Le RSA ne permet aussi de faire des signatures pour approuver des données. En effet dans une communication entre deux tiers, chacun peut signer ces message avec sa clé privé d et les destinataires peuvent vérifier cette signatuer avec la clé publique e. Exemple: Bob et Alice s'échangent des messages, chacun connait la clé publique de l'autre mais ils ne sont pas sur de la provenance de leur message. Chacun peut envoyer à chaque message le chiffrement de c avec sa clé privé,puis lors de la réception des messages, déchiffre c avec sa clé privé et c chiffré avec la clé publique de l'envoyeur, si c chiffré vaut c, alors la signature est vérifié. </p>
