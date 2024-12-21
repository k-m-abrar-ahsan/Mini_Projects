const input = document.querySelector(".input__field");
const inputIcon = document.querySelector(".input__icon");
const passwordStrength = document.querySelector(".progress-bar");

// Toggle password visibility
inputIcon.addEventListener("click", (e) => {
  e.preventDefault();

  input.setAttribute(
    "type",
    input.getAttribute("type") === "password" ? "text" : "password"
  );

  inputIcon.setAttribute(
    "src",
    input.getAttribute("type") === "password"
      ? "images/eye.png"
      : "images/eyeoff.png"
  );
});

// Check password strength on keyup
input.addEventListener("keyup", function () {
  let pass = document.getElementById("password").value;
  checkStrength(pass);
});

const progressBarClasses = [
  "progress-bar-danger",
  "progress-bar-warning",
  "progress-bar-success",
];

const handlePasswordStrengthClasses = (className, style) => {
  const classesToRemove = progressBarClasses.filter(
    (barClass) => barClass !== className
  );

  classesToRemove.forEach((barClass) => {
    passwordStrength.classList.remove(barClass);
  });

  passwordStrength.classList.add(className);
  passwordStrength.style = style;
};

const checkStrength = (password) => {
  let strength = 0;

  const passwordRule = (rule, ruleClass, strength) => {
    if (rule) {
      strength += 1;
      const img = document.querySelector(`.${ruleClass} img`);
      img.src = "images/green.jpg";
    } else {
      const img = document.querySelector(`.${ruleClass} img`);
      img.src = "images/red.png";
    }
    return strength;
  };

  strength = passwordRule(
    password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/),
    "low-upper-case",
    strength
  );
  strength = passwordRule(password.match(/([0-9])/), "one-number", strength);
  strength = passwordRule(
    password.match(/([!,@,#,$,%,^,&,*,?,_,~])/),
    "one-special-char",
    strength
  );
  strength = passwordRule(password.length > 7, "eight-character", strength);

  if (strength < 2) {
    handlePasswordStrengthClasses(progressBarClasses[0], "width: 10%");
  } else if (strength === 3) {
    handlePasswordStrengthClasses(progressBarClasses[1], "width: 60%");
  } else if (strength === 4) {
    handlePasswordStrengthClasses(progressBarClasses[2], "width: 100%");
  }
};
