// Select all p elements with the class 'two-two'
let cons = document.getElementsByClassName('two-two')[0].getElementsByTagName('p');

// console.log(cons);
// Add a class to each p element

for (let i = 0; i < cons.length; i++) {
    cons[i].addEventListener('mouseover', function() {
        // cons[i].style.transition = 'all 1s';
        cons[i].parentElement.style.display = 'flex';
        cons[i].parentElement.style.margin = 'auto';
        let di = document.createElement('div');
        di.style.width = '0%';
        di.style.height = '80%';
        di.style.margin = '3% 0';
        di.style.borderRadius = '10px';
        di.style.backgroundColor = 'red';
        cons[i].parentElement.appendChild(di);
        di.style.transition = 'all 1s'; // Add transition effect
        // di.style.transitionDelay = '1s'; // Add transition delay
        // di.style.opacity = '0'; // Set initial opacity
        setTimeout(() => {
            di.style.width = '60%';
            di.style.marginRight="3% "  // Increase opacity to 1 after delay
        }, 200);

        let di2 = document.createElement('div');
        di2.style.width = '30%';
        di2.style.height = '80%';
        di2.style.margin = '3% 0';
        di2.style.borderRadius = '10px';
        di2.style.backgroundColor = 'red';
        cons[i].parentElement.appendChild(di2);
        di2.style.transition = 'all 1s'; // Add transition effect
        // di2.style.transitionDelay = '1s'; // Add transition delay
        di2.style.opacity = '0'; // Set initial opacity
        setTimeout(() => {
            di2.style.opacity = '1'; // Increase opacity to 1 after delay
        }, 200);

        // Hide all other p elements
        for (let j = 0; j < cons.length; j++) {
            cons[j].style.display = 'none';
        }
        dii=document.createElement('div');
        dii.setAttribute('id', 'im');
        di.appendChild(dii);

        
        
         
    di.addEventListener('mouseout', function() {
        di.style.display = 'none';
        di2.style.display = 'none';
        // Show all other p elements
        for (let j = 0; j < cons.length; j++) {
            cons[j].style.display = 'block';
        }
    });
    
});
}