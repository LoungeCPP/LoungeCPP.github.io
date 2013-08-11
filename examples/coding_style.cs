#region Apache License 2.0

// Copyright 2013 Lounge<Chat> Team
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//   http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License. 

#endregion

namespace LoungeChat.Server.Components {
    using System;
    using System.Collections.Generic;

    using ThirdPartyLibrary;

    using Services;

    public sealed class Component : IService1, IService2 {
        private readonly ILog _logger;
        private int _test;

        private const string Something = "...";

        public int Test {
            get { return _test; }
            set { _test = value; }
        }

        public int Test2 { get; set; }

        public Component(ILog logger, IOtherDependency stuff) {
            _logger = logger;
        }

        private void Test() {
            throw new Exception("Abababa");
        }

        private void Test2() {
            try {
                Test();
            } catch (Exception e) {
                throw new Exception("blblblb", e);
            }
        }

        #region Implementation of IService1

        public void DoThing1() {
            _logger.Debug("Debug");
            _logger.Info("Start()");
            _logger.Warning("Warning");
            _logger.Error("Error");
            _logger.Fatal("Fatal");

            try {
                Test();
            } catch (Exception e) {
                _logger.Error(e, "Exception1");
            }

            try {
                Test2();
            } catch (Exception e) {
                _logger.Error(e, "Exception2");
            }

            foreach (var x in xs) {
            }

            for (var idx = 0; idx < xs.Length; ++idx) {
            }

            var soChatSucks = true;
            while (soChatSucks) {
            }
        }

        #endregion

        #region Implementation of IService2

        public void DoThing2() {
        }

        #endregion
    }
}
