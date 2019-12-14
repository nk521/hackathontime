<h1 align="center">HackathonTi.Me</h1>

<h3 align="center">Get.Set.[ Host || Participate].Flaunt!</h3>

<p align="center"> A <code>website</code> where you can host your hackathon or register for one! Participate to find your
  hackathon rankings. Aaaaaand help us improve!
</p>

<p align="center">
  <img src="https://img.shields.io/github/issues/nk521/hackathonti.me?style=flat-square&color=brightgreen&logo=github"
       alt="Github issues" />
  <img src="https://img.shields.io/github/languages/code-size/nk521/hackathonti.me?style=flat-square&color=orange"
       alt="Code size" />
  <img src="https://img.shields.io/github/license/nk521/hackathonti.me?style=flat-square&color=blueviolet"
       alt="License" />
</p> 

<h3 align="center">
  <a href="https://hackathonti-me.herokuapp.com/">
    Website
  </a>
  <span> | </span>
  <a href="https://github.com/nk521/hackathonti.me/blob/master/README.md#contribution-guide-i-want-to-get-started">
    Contributing
  </a>
</h3>

<p align="center">
  <sub>Built with ❤︎ by
    <a href="https://github.com/nk521">Nikhil Kumar</a> and others. Supported by You. 
    </a>
</p>

## `Idea` What are we thinking?
This platform caters to hackathon hosts and participants alike. 
- The home page shows ongoing and future hackathons.
- A host can mail us or fill a form to register a hackathon with required details. 
- Participants register at [Hackathonti.me](www.hackathonti.me) for the same hackathon or find a past event in the archive.
- Two hours after the hackathon ends, public voting takes place and registered users are able to vote for 24hrs. These factors include but are not limited to reliability, environment, growth potential, management.
- This decides the _points_, suppose average rating of hackathon is `x` (float). Consequently, the winning team scores `x` points, first runner up scores `x/2` points and second runner up will score `x/4`. 
- After every 4 months, ranks are calculated for these participant teams and individual hackathons. These ranks are your flaunt-o-meter!✨

## `Work already done` We did this much! 
- User Interface (UI). But it feels a little off-handed right now. Feel free to propose a change to this! ⬅️
- Pages for Login/Register into HackathonTi.Me.
- Logic for Creation and Joining of teams for hackathons by participants.
- Logic for Date/Time for hackathons to decide the ongoing, future and past events and move them to archive accordingly.
- Points for teams and hackathons. This is implemented manually at this moment.

## `Work in Progress` Still brainstorming these ones!
- Public Voting for hackathons.
- Is Team Blog is a good idea? Essentially, this will be a place where teams can write about their projects to maintain a project archive. The information for the team like [ team members, hackathons went and hackathons attending ] could, hence, be more concisely arranged on the page. [ If you would like to work on this idea, find models/forms/views in `hackathontime_users` directory. They have purposely been commented out. ] 

## `Screenshots` How do we look like?
(Will be added super soon)

## `Contribution Guide` I want to get started. 
If you would like to update resources on Hackathonti.Me, please:
- Find an issue with a label relevant to your interest.
- Make a fork of this repository.
- Clone your fork locally.
- Create a new branch to contain your change. Give your branch a descriptive name, such as `team-blog-bug-fix`, or `date-logic-fix`.
- Make your change using the browser or on your local machine.
- Commit your change.
- Push the branch to your remote fork.
- Make a pull request to the original repo.

If you are not sure how to complete the above steps, GitHub's [Fork a Repo guide](https://help.github.com/en/articles/fork-a-repo#fork-an-example-repository) is a good place to start.

## `Setup Guide` Let's get to work.
- Make sure your local machine has Python3.6+ pre-installed.
- Start with installing `virtualenv` and creating a `virtualenv` for this project. 
- Clone this repo and install the other requirements. 
- Set some enviornment variables and then migrate the models. Tada! 🙌

```
    # install and make a virtualenv
    python3 -m pip install virtualenv
    python3 -m virtualenv <name>
    source <name>/bin/activate

    # clone the repo
    git clone https://github.com/nk521/hackathonti.me
    cd hackathonti.me

    # install requirements
    python -m pip install requirements.txt

    # now migrate
    python manage.py makemigrations
    python manage.py migrate

    # create superuser and run server
    python manage.py createsuperuser
    python manage.py runserver
```

If you encounter any errors regarding database after accessing the website on localhost, try to migrate the models again.

## `Future Plans` Wanting more!
You tell this. What feature would you like to propose? Go ahead and open an issue for feature request. 😀🧙

### Let us know how we did.
Drop in a mail at 📩 admin@hackathonti.me with your suggestions.

Or simply report a bug 🐞. Find guides and friendly templates from Github here: 
- [creating-an-issue](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue)
- [incorporating-feedback-in-your-pr](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/incorporating-feedback-in-your-pull-request#opening-an-issue-for-an-out-of-scope-suggestion)

#### Watch 👀. Star ⭐. Fork 🍴.
