Thực tập team Platform Services

Vị trí:

* Dev
* Ops

#**1. Thống kê tỷ lệ browser**

Cho file nginx access log: https://gist.github.com/anonymous/9f9bd99d2f32914d033a

log format:

$remote_addr $http_x_forwarded_for [$time_iso8601] $http_host "$request" $status $bytes_sent "$http_referer" "$http_user_agent" $gzip_ratio $request_length $request_time


Viết script python thống kê tỷ lệ truy cập theo loại browser (dựa vào user agent)

#**2. Convert log sang Common Log Format-**

-Cho file log https://www.dropbox.com/s/a6ip48kn0ngelml/access.log?dl=0-

-Viết script common_log_format.py nhận dòng log từ stdin, convert sang common log format (https://en.wikipedia.org/wiki/Common_Log_Format) và print ra màn hình-

-$ cat access.log | python common_log_format.py-

#**3. Script chặn tấn công DDoS Level 7 đơn giản**

Cho file nginx access log (log format mặc định): https://www.dropbox.com/s/a6ip48kn0ngelml/access.log?dl=0

Viết script python lọc ra các IP request GET quá 120 requests (link text/html)/1 phút & đưa các IP đó vào iptables để chặn

Ghi chú:

* thời gian chạy script dưới 60 giây
* script được đặt trong crontab chạy 1 phút 1 lần
* file log đặt ở /var/log/nginx/access.log
* không chặn các request từ google, bing, facebook
* phân biệt được những IP giả mạo user agent google, bing, facebook
* tối ưu iptables để chặn được > 10k IPs
* IP chặn expires sau 7 ngày
* tạo repo, commit & push lên github

#**4. Service đếm unique user agents**

Viết 1 web app chạy ở port 80, nhận request HTTP request bất kỳ, đếm và trả ra số lượng unique user agent hiện tại (theo từng ngày)

Yêu cầu:

* Dùng flask, redis
* Tham khảo HyperLogLog - http://antirez.com/news/75
* Dùng PFADD, PFCOUNT
* Dùng nginx làm load balancer
* Dùng supervisord để quản lý (bật, tắt) các process redis, python, nginx
* Dùng apache benchmark (ab) hoặc wrk phải đạt > 2000 requests/giây
* Dùng ansible để deploy toàn bộ project này lên 1 server ubuntu 14.04 (tự cài virtualbox để test)

#**5. Thống kê tỷ lệ SSL protocol/cipher**

Cho file log /var/log/nghttp2/access.log, log format:

$time_iso8601 $http_host $alpn $ssl_protocol $ssl_cipher

https://gist.github.com/andy-pham/981211ed3361a732a253

File log được ghi liên tục, dung lượng > 5GB. Viết script python thống kê SSL protocol/cipher của phút vừa rồi, sử dụng ít hơn 512MB RAM.


Kế hoạch training & thời gian:

Tổng thời gian

* 3 tháng (12 tuần)
* 1 tháng đầu: **thực tập không lương** full time
* 2 tháng tiếp theo: **thử việc có lương**
* sau 2 tháng thử việc sẽ quyết định **ký hợp đồng chính thức** hoặc **ngừng thử việc**

Timeline

* Tuần 1: Giới thiệu
* Tuần 2: Python cơ bản
* Tuần 3: Git nâng cao, HA & scalability
* Tuần 4: Ansible
* Tuần 5: Integration tests 
* Tuần 6-12: Làm project thực tế
    * Các tiêu chí đánh giá:
        * cách thức giao tiếp
        * git log
        * coding style
        * logic
        * tổ chức project
        * code chạy hay không?
    * Kết thúc:
        * ký hợp đồng lao động chính thức
        * hoặc ngừng thực tập

Tài liệu & nguồn kiến thức tham khảo:

* Chung
    * High Scalability: http://highscalability.com/all-time-favorites/
    * Git Workflow: https://gist.github.com/andy-pham/4a458a780fcfe8a00209
    * README driven development: http://tom.preston-werner.com/2010/08/23/readme-driven-development.html
    * Markdown: https://guides.github.com/features/mastering-markdown/
    * Security Checklist: Security Checklist (https://quip.com/d6aIAzwuScmR)
    * GIFs:
        * http://thecodinglove.com (http://thecodinglove.com/)
        * http://devopsreactions.tumblr.com (http://devopsreactions.tumblr.com/)
    * Continuous Delivery: https://puppetlabs.com/sites/default/files/CDebook.pdf
    * Hacker News: https://news.ycombinator.com/best
    * Lists of Top Quora Content: https://www.quora.com/Lists-of-Top-Quora-Content
    * List of must read articles for modern web development: http://blog.arvidandersson.se/2014/06/17/best-practices-in-modern-web-projects
* Dev
    * Python Guide: http://docs.python-guide.org/en/latest/
    * http://learnpythonthehardway.org/book/
* Ops
    * Ops School: http://www.opsschool.org/en/latest/
    * Web Operations - Keeping the Data On Time: http://goo.gl/dcwFxu

Các kỹ năng cần có:

* Giao tiếp trong team: 
    * Gọi nhiều lần: lỗi nghiêm trọng, liên quan trực tiếp
    * Gọi 1 lần: hỏi nhanh
    * SMS: gọi không được
    * Chat: mọi thứ khác
        * Ưu tiên chat vào group
        * Không chat 1-1
        * “Don’t ping, just ask”
    * http://heeris.id.au/2013/this-is-why-you-shouldnt-interrupt-a-programmer/
* Sử dụng Linux (Ubuntu, Centos, Fedora...)
* Sử dụng dòng lệnh (bash, zsh, fish)
    * ls, cd, pgrep, pkill, kill, vim
    * echo, chown, chmod, grep
    * tar, unzip, screen, tmux, atop, df, du
    * curl, wget, clear, history
    * rsync, scp, rm, cp, mv, ssh, touch
    *  cat, zcat, tac, tail, head, cut, sort, uniq, wc
* Shell script đơn giản
    * Hello World! using variables
    * For loop
* Python cơ bản
    * Python 2.7
    * Cài PyCharm (bản community - https://www.jetbrains.com/pycharm/download/)
    * http://www.learnpython.org (http://www.learnpython.org/)
        * Hello, World! (http://www.learnpython.org/en/Hello%2C_World%21)
        * Variables and Types (http://www.learnpython.org/en/Variables_and_Types)
        * Lists (http://www.learnpython.org/en/Lists)
        * Basic Operators (http://www.learnpython.org/en/Basic_Operators)
        * String Formatting (http://www.learnpython.org/en/String_Formatting)
        * Basic String Operations (http://www.learnpython.org/en/Basic_String_Operations)
        * Conditions (http://www.learnpython.org/en/Conditions)
        * Loops (http://www.learnpython.org/en/Loops)
        * Functions (http://www.learnpython.org/en/Functions)
        * Dictionaries (http://www.learnpython.org/en/Dictionaries)
        * Modules and Packages (http://www.learnpython.org/en/Modules_and_Packages)
        * (chưa cần học phần “Classes and Objects” - mình ít khi dùng OOP)
    * Evolution of a Python programmer: https://gist.github.com/fmeyer/289467
        * (viết kiểu Newbie, Lazy hoặc Expert là ok)
    * Code Style (http://docs.python-guide.org/en/latest/writing/style/)
    * Các thư viện hay dùng:
        * os.path
        * sys.argv
        * time, datetime
        * base64
        * hashlib
        * re
        * json/simplejson
        * requests
        * py.test
        * tox
        * flask
        * jinja2
        * virtualenv
        * pip install/uninstall/freeze
        * supervisord
* Git cơ bản:
    * Atomic commits: http://seesparkbox.com/foundry/atomic_commits_with_git
    * Check in early, check in often: http://blog.codinghorror.com/check-in-early-check-in-often/
    * Các lệnh thường dùng
        * git status
        * git checkout
        * git checkout -b
        * git pull —rebase
        * git push
        * git log
        * git merge
* Các công cụ hay dùng:
    * ansible
    * nginx
    * redis
    * memcached
    * mongodb
    * mysql
    * sentry
    * ipython
